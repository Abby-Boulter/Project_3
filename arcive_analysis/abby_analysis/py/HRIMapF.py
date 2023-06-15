#Imports
import numpy as np
import json
import pandas as pd
import plotly
import plotly.graph_objs as go
import chart_studio.plotly as py
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../hri.sqlite")

#Reflect an existing database into a new model
Base = automap_base()
#Reflect the tables
Base.prepare(autoload_with=engine)

#Save reference to the table
ext = Base.classes.extreme_heat_days
ed_visit = Base.classes.ed_visit_35

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
#Flask Routes
#################################################

@app.route("/")
def home():
    #List all available api routes.
    return (
        f"Available Routes for Heat Related Illnesses in AZ:<br/>"
        f"- Heat Related illnesses: <a href=\"/extreme\">Extreme<a><br/>"
        # f"- HRI data in a Map: <a href=\"/hriMap\">HRI Map<a><br/>"
        #f"- Daily Temperature Observations for Station USC00519281 for 2016-2017 Season: <a href=\"/api/v1.0/tobs\">/api/v1.0/tobs<a><br/>"
        #f"- Enter a start date between 2010-01-01 and 2017-08-23 to get the minimum, maximum, and average temperatures for all dates after the specified date: /api/v1.0/yyyy-mm-dd<br>"
        #f"- Enter both a start and end date between 2010-01-01 and 2017-08-23 to get the minimum, maximum, and average temperatures for that date range: /api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br>"
    )

#HRI Route
@app.route("/extreme")
def extremeH():
    #Create our session (link) from Python to the DB
    session = Session(engine)

    #Return a list of ED rates and year
    ext_sess  = session.query(ext.county, ext.year, ext.ext_heat_days)

    session.close()

    #Put values into a dictionary to be displayed.
    ext_values = []
    for ct, yr, rt in ext_sess:
        ext_dict = {}
        ext_dict["county"] = ct
        ext_dict["year"] = yr
        ext_dict["ED_rates"] = rt
        ext_values.append(ext_dict)

    #display jsonified results
    return jsonify(ext_values) 


#HRIMap Route
# @app.route("/hriMap")
# def ed_visit2():

    # session = Session(engine)

    # #Return a DataFrame to buid a choropleth map
    # df = session.query(ed_visit2.GeogID, ed_visit2.year, ed_visit2.ed_rate)


if __name__ == '__main__':
    app.run(debug=True)
