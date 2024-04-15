from flask import Flask, render_template
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    # Generate some example data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # Create the plot
    plt.figure()
    plt.plot(x, y1, label='Sin(x)')
    plt.plot(x, y2, label='Cos(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sin(x) and Cos(x)')
    plt.legend()

    # Save the plot as an image
    plot_path = 'static/plot.png'  # Save the plot in the 'static' folder
    plt.savefig(plot_path)

    # Render the webpage with the plot image
    return render_template('index.html', plot_path=plot_path)
