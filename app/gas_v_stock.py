#import pandas as pd
import matplotlib.pyplot as plt
import oracledb
#import plotly.express as px


def get_db_connection():
    dsn = oracledb.makedsn('oracle.cise.ufl.edu', 1521, sid='orcl')  # should be the same
    un = 'ncomatas'  # oracle username (ufl)
    pw = 'BTnup3sP9GzEcT64Tec4pLBD'  # oracle password (from CISE)
    conn = oracledb.connect(user=un, password=pw, dsn=dsn)
    return conn


# EACH QUERY HAS A FUNCTION CALL WITH INPUTS
def get_gas_prices(company, region):
    conn = get_db_connection()

    # SQL query
    query = f"""with avgStockPrices as (
    SELECT EXTRACT(YEAR FROM closedate) AS year, round(avg(price), 2) as PricePerShare
    FROM stocks
    WHERE ticker in ('{company}')
    GROUP BY EXTRACT(YEAR FROM closedate), ticker
    ORDER BY year),
avgUSGasPrices as (
    SELECT EXTRACT(YEAR FROM gasdate) AS year, round(avg(price), 2) as GasPrice
    FROM gas_prices
    WHERE regionname in ('{region}')
    GROUP BY EXTRACT(YEAR FROM gasdate), regionname
    ORDER BY year)
select avgStockPrices.year, avgStockPrices.PricePerShare, avgUSGasPrices.GasPrice
from avgStockPrices join avgUSGasPrices
on avgUSGasPrices.year = avgStockPrices.year
"""

    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


# def create_price_trend_graph():
#     data = get_gas_prices()
#     df = pd.DataFrame(data, columns=['price_date', 'price'])
#     fig = px.line(df, x='price_date', y='price', title='Gas Price Trends Over Time')
#     graph_html = fig.to_html(full_html=False)
#     return graph_html


# @app.route('/price_trends')
# def price_trends():
#     graph_html = create_price_trend_graph()
#     return render_template('price_trends.html', graph=graph_html)


data = get_gas_prices("XOM", "U.S.")
# print(data)

years = []
pps = []
gasprice = []

for tuple in data:
    years.append(tuple[0])
    pps.append(tuple[1])
    gasprice.append(tuple[2])

# Step 3: Select Data for Axes
x_axis_column = 'year'
y_axis_columns = ['Stock Price Per Share of', 'Price of Gas'] # DETERMINES NAME ON LEGEND

x_axis = years
y_axes = [pps, gasprice]

# Step 4: Create Plot
for y_axis in y_axes:
    plt.plot(x_axis, y_axis)

# Step 5: Customize Plot (Optional)
plt.xlabel('Year')
plt.ylabel('Value in $$$')
plt.title('Gas Price VS Stock Values')

# Step 6: Display Plot
plt.legend(y_axis_columns)  # Add legend for clarity
plt.show()
