#Imports
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hri.sqlite")

#Reflect an existing database into a new model
Base = automap_base()
#Reflect the tables
Base.prepare(autoload_with=engine)

#Save reference to the table
hri_table = Base.classes.hri

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
def hri():
    #Create our session (link) from Python to the DB
    session = Session(engine)

    #Return a list of all precipitation
    hri_sess  = pd.DataFrame(session.query(hri_table.year, hri_table.ED_rates))

    session.close()


    return hri_sess['']



#HRIMap Route
@app.route("/hriMap")
def hriMap():
    #Create our session (link) from Python to the DB
    session = Session(engine)
    df = pd.DataFrame(session.query(hri_table.county, hri_table.year, hri_table.ED_rates))
# min year in your dataset
year = 2011

# your color-scale
scl = [[0.0, '#ffffff'],[0.2, '#b4a8ce'],[0.4, '#8573a9'],
       [0.6, '#7159a3'],[0.8, '#5732a1'],[1.0, '#2c0579']] # purples


data_slider = []
for year in df['year'].unique():
    df_segmented =  df[(df['year']== year)]

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


if __name__ == '__main__':
    app.run(debug=True)