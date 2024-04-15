from flask import render_template, request, jsonify
from app import app, db_session  # Ensure 'db' is your SQLAlchemy database instance
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from app.models import GasPrice
from io import BytesIO
import base64
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
@app.route('/trend_analysis')
def trend_analysis():
    fuel_types = [fuel_type[0] for fuel_type in db_session.query(GasPrice.fuel_type.distinct()).all()]
    regions = [region[0] for region in db_session.query(GasPrice.region.distinct()).all()]
    return render_template('trend_analysis.html', fuel_types=fuel_types, regions=regions)

@app.route('/trend_analysis/data', methods=['POST'])
def trend_analysis_data():
    fuel_type = request.form.get('fuel_type')
    region = request.form.get('region')
    from_date = request.form.get('from_date')
    to_date = request.form.get('to_date')

    data = GasPrice.query \
        .filter(GasPrice.fuel_type == fuel_type, GasPrice.region == region) \
        .filter(GasPrice.gasdate.between(from_date, to_date)) \
        .order_by(GasPrice.gasdate.asc()) \
        .all()

    # Generate the plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot([point.gasdate for point in data], [point.price for point in data])
    axis.set_title('Gas Price Trends')
    axis.set_xlabel('Date')
    axis.set_ylabel('Price')

    # Convert plot to PNG image
    png_image = BytesIO()
    FigureCanvas(fig).print_png(png_image)

    # Encode PNG image to base64 string
    png_image_b64_string = "data:image/png;base64," + base64.b64encode(png_image.getvalue()).decode('ascii')
    
    return jsonify({'image': png_image_b64_string})