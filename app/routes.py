from flask import render_template
from app import create_app
from app.gas_v_stock import get_gasprices_v_stockprices
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
    # Example usage, replace 'XOM' and 'U.S.' with dynamic values as needed
    plot_path = get_gasprices_v_stockprices("XOM", "U.S.")
    return render_template('gasprice_stock_comparison.html', plot_path=plot_path)

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