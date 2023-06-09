#Imports
import numpy as np
import pandas as pd
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
engine = create_engine("sqlite:///..data/hri.sqlite")

#Reflect an existing database into a new model
Base = automap_base()
#Reflect the tables
Base.prepare(autoload_with=engine)

#Save reference to the table
hri = Base.classes.hri
ed_visit = Base.classes.ed_visit
hospitalization = Base.classes.hospitalization
vulnerability = Base.classes.vulnerability
ed_visit_35 = Base.classes.ed_visit_35


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
        f"- Daily Precipitation for 2016-2017 Season: <a href=\"/hri\">HRI<a><br/>"
        #f"- Weather Stations: <a href=\"/api/v1.0/stations\">/api/v1.0/stations<a><br/>"
        #f"- Daily Temperature Observations for Station USC00519281 for 2016-2017 Season: <a href=\"/api/v1.0/tobs\">/api/v1.0/tobs<a><br/>"
        #f"- Enter a start date between 2010-01-01 and 2017-08-23 to get the minimum, maximum, and average temperatures for all dates after the specified date: /api/v1.0/yyyy-mm-dd<br>"
        #f"- Enter both a start and end date between 2010-01-01 and 2017-08-23 to get the minimum, maximum, and average temperatures for that date range: /api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br>"
    )

#HRI Route
@app.route("/hri")
def precipitation():
    #Create our session (link) from Python to the DB
    session = Session(engine)

    #Return a list of all precipitation
    hri  = session.query(hri.year, hri.ED_Rates)

    session.close()

    #Convert precipitation analysis to a dictionary using date as the key and prcp as the value.
    hri_values = []
    for yr, rt in hri:
        hri_dict = {}
        hri_dict["year"] = yr
        hri_dict["ED_Rates"] = rt
        hri_values.append(hri_dict)

    return jsonify(hri_values) 
 

# min year in your dataset
year = 1998

# your color-scale
scl = [[0.0, '#ffffff'],[0.2, '#b4a8ce'],[0.4, '#8573a9'],
       [0.6, '#7159a3'],[0.8, '#5732a1'],[1.0, '#2c0579']] # purples

data_slider = []
for year in df['years'].unique():
    df_segmented =  df[(df['years']== year)]

    for col in df_segmented.columns:
        df_segmented[col] = df_segmented[col].astype(str)

    data_each_yr = dict(
                        type='choropleth',
                        locations = df_segmented['state'],
                        z=df_segmented['sightings'].astype(float),
                        locationmode='USA-states',
                        colorscale = scl,
                        colorbar= {'title':'# Sightings'})

    data_slider.append(data_each_yr)

steps = []
for i in range(len(data_slider)):
    step = dict(method='restyle',
                args=['visible', [False] * len(data_slider)],
                label='Year {}'.format(i + 1998))
    step['args'][1][i] = True
    steps.append(step)

sliders = [dict(active=0, pad={"t": 1}, steps=steps)]

layout = dict(title ='UFO Sightings by State Since 1998', geo=dict(scope='usa',
                       projection={'type': 'albers usa'}),
              sliders=sliders)

fig = dict(data=data_slider, layout=layout)
periscope.plotly(fig)

if __name__ == '__main__':
    app.run(debug=True)