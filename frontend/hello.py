from flask import Flask
from flask import render_template
from datetime import time


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# c3.js
@app.route('/front1')
def frontend():
    return render_template('frontend_c3.html')


# Chart.js
@app.route("/simple_chart")
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, -60, 4, -7, 100]
    return render_template('chart.html', values=values, labels=labels, legend=legend)
