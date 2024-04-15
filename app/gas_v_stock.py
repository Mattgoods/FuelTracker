#import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import oracledb
#import plotly.express as px
import os

def get_db_connection():
    dsn = oracledb.makedsn('oracle.cise.ufl.edu', 1521, sid='orcl')  # should be the same
    un = 'ncomatas'  # oracle username (ufl)
    pw = 'BTnup3sP9GzEcT64Tec4pLBD'  # oracle password (from CISE)
    conn = oracledb.connect(user=un, password=pw, dsn=dsn)
    return conn


# EACH QUERY HAS A FUNCTION CALL WITH INPUTS
def get_gasprices_v_stockprices(company, region):
    conn = get_db_connection()

    query = f"""
    WITH avgStockPrices AS (
        SELECT EXTRACT(YEAR FROM closedate) AS year, ROUND(AVG(price), 2) AS PricePerShare
        FROM stocks
        WHERE ticker IN ('{company}')
        GROUP BY EXTRACT(YEAR FROM closedate), ticker
        ORDER BY year),
    avgUSGasPrices AS (
        SELECT EXTRACT(YEAR FROM gasdate) AS year, ROUND(AVG(price), 2) AS GasPrice
        FROM gas_prices
        WHERE regionname IN ('{region}')
        GROUP BY EXTRACT(YEAR FROM gasdate), regionname
        ORDER BY year)
    SELECT avgStockPrices.year, avgStockPrices.PricePerShare, avgUSGasPrices.GasPrice
    FROM avgStockPrices JOIN avgUSGasPrices
    ON avgUSGasPrices.year = avgStockPrices.year
    """

    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    if not data:
        return None  # or handle this case as you see fit

    years, pps, gasprice = zip(*data)  # Unpacking data

    # Create Plot
    plt.figure()
    plt.plot(years, pps, label='Stock Price Per Share of ' + company)
    plt.plot(years, gasprice, label='Price of Gas in ' + region)
    plt.xlabel('Year')
    plt.ylabel('Value in $')
    plt.title(f'Gas Price VS Stock Values of {company}')
    plt.legend()

    # Set the path to the 'static/graphs' directory and create if it doesn't exist
    
    # Save the plot in 'static/graphs' directory
    plot_path = 'plot_gas_vs_stock.png'
    plt.savefig(plot_path)
    plt.close()  # Ensure matplotlib does not hold onto the figure
    print(plot_path)
    return plot_path
   