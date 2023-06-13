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
engine = create_engine("sqlite:///../data/hri.sqlite")

#Reflect an existing database into a new model
Base = automap_base()
#Reflect the tables
Base.prepare(autoload_with=engine)

#Save reference to the table
hri_table = Base.classes.hri
ed_visit2 = Base.classes.ed_visit2

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
        f"- Heat Related illnesses: <a href=\"/hri\">HRI<a><br/>"
        f"- HRI data in a Map: <a href=\"/hriMap\">HRI Map<a><br/>"
        #f"- Daily Temperature Observations for Station USC00519281 for 2016-2017 Season: <a href=\"/api/v1.0/tobs\">/api/v1.0/tobs<a><br/>"
        #f"- Enter a start date between 2010-01-01 and 2017-08-23 to get the minimum, maximum, and average temperatures for all dates after the specified date: /api/v1.0/yyyy-mm-dd<br>"
        #f"- Enter both a start and end date between 2010-01-01 and 2017-08-23 to get the minimum, maximum, and average temperatures for that date range: /api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br>"
    )

#HRI Route
@app.route("/hri")
def hri():
    #Create our session (link) from Python to the DB
    session = Session(engine)

    #Return a list of ED rates and year
    hri_sess  = session.query(hri_table.year, hri_table.ED_rates)

    session.close()

    #Put values into a dictionary to be displayed.
    hri_values = []
    for yr, rt in hri_sess:
        hri_dict = {}
        hri_dict["year"] = yr
        hri_dict["ED_rates"] = rt
        hri_values.append(hri_dict)

    #display jsonified results
    return jsonify(hri_values) 


#HRIMap Route
# @app.route("/hriMap")
# def ed_visit2():

#     session = Session(engine)

#     #Return a DataFrame to buid a choropleth map
#     df = session.query(ed_visit2.GeogID, ed_visit2.year, ed_visit2.ed_rate)

#     session.close()

#     data = [dict(type='choropleth', 
#             locations = df['GeogID'].astype(str),
#             z=df['ED_rates'].astype(float),
#             geojson='../data/arizona-with-county-boundaries_1085.geojson')]
#     steps = []

#     for i in range(len(data)):
#         step = dict(method='restyle',
#                     args=['visible', [False] * len(data)],
#                     label='Year {}'.format(i + 2011))
#         step['args'][1][i] = True
#         steps.append(step)

# sliders = [dict(active=0, pad={"t": 1}, steps=steps)]


@app.route("/countiesjson")
def test():
    with open('data/arizona-with-county-boundaries_1085.geojson','r') as gdata:
        geojson = json.load(gdata)
        print(geojson)

        return geojson

if __name__ == '__main__':
    app.run(debug=True)
