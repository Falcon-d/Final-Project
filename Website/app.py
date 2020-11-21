# import necessary libraries
import os
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

engine = create_engine(os.environ.get('DATABASE_URL', ''))


# engine = create_engine(f'postgres://osifuxgjnarnus:a02625bbbff82478924acd4f8bee4105c3931e214c799ee67df98ca31fb47ddd@ec2-3-220-98-137.compute-1.amazonaws.com:5432/deed6otvdvkm17')

Base = automap_base()
Base.prepare(engine, reflect=True)

Stocks = Base.classes.historical_and_results

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


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
    open = [result[2] for result in results]
    datatable.append(open)
    high = [result[3] for result in results]
    datatable.append(high)
    low = [result[4] for result in results]
    datatable.append(low)

    dataresults={"results": datatable}
    return jsonify (dataresults) 

if __name__ == "__main__":
    app.run()
