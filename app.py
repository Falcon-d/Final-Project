# import necessary libraries
import os
import pickle
import numpy as np
import pmdarima
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

#from config import username, password

# engine = create_engine(os.environ.get('DATABASE_URL', ''))


engine = create_engine(f'postgres://osifuxgjnarnus:a02625bbbff82478924acd4f8bee4105c3931e214c799ee67df98ca31fb47ddd@ec2-3-220-98-137.compute-1.amazonaws.com:5432/deed6otvdvkm17')

Base = automap_base()
Base.prepare(engine, reflect=True)

Stocks = Base.classes.historical_and_results

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

model = pickle.load(open('ARIMA.pkl','rb'))

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyzer")
def analyzer():
    return render_template("analyzer.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/visualizations")
def visualizations():
    return render_template("visualizations.html")

@app.route("/api/datatable")
def datatable():

    session = Session(engine)
    datatable=[]
    results = session.query(Stocks.date, Stocks.close, Stocks.open, Stocks.high, Stocks.low).all()
    
    date = [result[0] for result in results]
    datatable.append(date)
    close = [result[1] for result in results]
    datatable.append(close)
    open = [result[3] for result in results]
    datatable.append(open)
    high = [result[4] for result in results]
    datatable.append(high)
    low = [result[5] for result in results]
    datatable.append(low)
    predicted = [result[6] for result in results]
    datatable.append(predicted)
    actual = [result[7] for result in results]
    datatable.append(actual)
    diference = [result[8] for result in results]
    datatable.append(diference)

    dataresults={"results": datatable}
    return jsonify (dataresults) 

@app.route('/api',methods=['POST'])
def predict():
# Get the data from the POST request.
    if request.method == "POST":
        form_data = request.form
# # Make prediction using model loaded from disk as per the data.
    prediction = model.predict(int(form_data['Day']))
# # Take the first value of prediction
    output = prediction[-1]
    return jsonify(output)


if __name__ == "__main__":
    app.run()
