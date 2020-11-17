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

from config import username, password

#engine = create_engine(os.environ.get('DATABASE_URL', ''))


engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/Project2')

Base = automap_base()
Base.prepare(engine, reflect=True)

Stock = Base.classes.Stock

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

@app.route("/")
def visualizations():
    return render_template("visualizations.html")

if __name__ == "__main__":
    app.run()
