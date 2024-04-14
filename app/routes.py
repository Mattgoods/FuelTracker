from flask import render_template
from app import create_app

app = create_app()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/price_trends')
def price_trends():
    # Return price trends page
    pass

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