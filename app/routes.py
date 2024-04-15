from flask import render_template, url_for
from app.gas_v_stock import get_gasprices_v_stockprices
from . import create_app

app = create_app()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/price_trends')
def price_trends():
    # Return price trends page
    pass

@app.route('/gasprice-stock-comparison')
def gasprice_stock_comparison():
    plot_filename = get_gasprices_v_stockprices("XOM", "U.S.")
    return render_template('gasprice_stock_comparison.html', plot_filename=plot_filename)


@app.route('/factor_analysis')
def factor_analysis():
    # Return factor analysis page
    pass

@app.route('/regional_comparison')
def regional_comparison():
    # Return regional comparison page
    pass

@app.route('/settings')
def settings():
    # Return settings page
    pass