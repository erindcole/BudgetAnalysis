from flask import Flask, jsonify
from flask import render_template
from datetime import time
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# c3.js
# area charts
@app.route('/front1')
def frontend():
    return render_template('frontend_c3.html')

# read from json endpoint 
# this method uses the {{ ... |safe}} method of getting the json passed
@app.route('/json_read', methods=['GET', 'POST'])
def json_read():
    x = {'x': ['01/01/2018', '01/02/2018', '01/05/2018', '01/19/2018', '02/04/2018', '03/05/2018']}
    income = {'income': [30, 200, 100, 400, 150, 250]}
    expense = {'expense': [50, 20, 10, 40, 15, 25]}
    return render_template('load_from_json.html', x=json.dumps(x), income=json.dumps(income), expense=json.dumps(expense))

########################################################################
# not going thru with this route
@app.route('/json_read_endpoint', methods=['GET', 'POST'])
def json_read_endpoint():
  return render_template('json_endpoint.html')

# endpoint emitting json 
# so this route kind of takes a while for the read endpoint to get the data
# also, im thinking the data is maybe not in a recognizable format for d3.json
@app.route('/json_endpoint', methods=['GET', 'POST'])
def json_endpoint():

    x = {'x': ['01/01/2018', '01/02/2018', '01/05/2018', '01/19/2018', '02/04/2018', '03/05/2018']}
    income = {'income': [30, 200, 100, 400, 150, 250]}
    expense = {'expense': [50, 20, 10, 40, 15, 25]}
    data = dict({ 'x':x['x'], 'income':income['income'], 'expense':expense['expense'] })
    return jsonify(data)
########################################################################




# Chart.js
@app.route("/simple_chart")
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, -60, 4, -7, 100]
    return render_template('chart.html', values=values, labels=labels, legend=legend)
