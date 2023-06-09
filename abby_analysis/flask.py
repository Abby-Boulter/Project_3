#Imports
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#Reflect an existing database into a new model
Base = automap_base()
#Reflect the tables
Base.prepare(autoload_with=engine)

#Save reference to the table
meas = Base.classes.measurement
stat = Base.classes.station

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
        f"Available Routes for HI Weather:<br/>"
        f"- Daily Precipitation for 2016-2017 Season: <a href=\"/api/v1.0/precipitation\">/api/v1.0/precipitation<a><br/>"
        f"- Weather Stations: <a href=\"/api/v1.0/stations\">/api/v1.0/stations<a><br/>"
        f"- Daily Temperature Observations for Station USC00519281 for 2016-2017 Season: <a href=\"/api/v1.0/tobs\">/api/v1.0/tobs<a><br/>"
        f"- Enter a start date between 2010-01-01 and 2017-08-23 to get the minimum, maximum, and average temperatures for all dates after the specified date: /api/v1.0/yyyy-mm-dd<br>"
        f"- Enter both a start and end date between 2010-01-01 and 2017-08-23 to get the minimum, maximum, and average temperatures for that date range: /api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br>"
    )

#Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    #Create our session (link) from Python to the DB
    session = Session(engine)

    #Return a list of all precipitation
    last_yr_prcp  = session.query(meas.date, meas.prcp).filter(meas.date <= '2017-08-23').\
        filter(meas.date > '2016-08-23').order_by(meas.date).all()

    session.close()

    #Convert precipitation analysis to a dictionary using date as the key and prcp as the value.
    precip_values = []
    for prcp, date in last_yr_prcp:
        precip_dict = {}
        precip_dict["precipitation"] = prcp
        precip_dict["date"] = date
        precip_values.append(precip_dict)

    return jsonify(precip_values) 
 
 #Station Route
@app.route("/api/v1.0/stations")
def station(): 
    session = Session(engine)
    
    #Return a list of stations from the database
    active_stations = session.query(meas.station).\
        group_by(meas.station).all()
    session.close()
    
    stations_list = list(np.ravel(active_stations))
    return jsonify (stations_list)

#Tobs Route
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    
    # query: the most active stations last year 
    active_station= session.query(meas.station, func.count(meas.station)).\
        order_by(func.count(meas.station).desc()).group_by(meas.station).first()
    
    #most active station ID
    most_active_station = active_station[0] 

    session.close()
    
    #only the most active station: 
    print(most_active_station)
    
    tobs_most_active = session.query(meas.date, meas.tobs, meas.station).\
        filter(meas.date > '2016-08-23').filter(meas.station == most_active_station) 
    
    # Create a list of dates,tobs,and stations that will be appended with dictionary values for date, tobs, and station number queried above
    tobs_values = []
    for date, tobs, station in tobs_most_active:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_dict["station"] = station
        tobs_values.append(tobs_dict)
        
    return jsonify(tobs_values) 

# Dynamic Route accepts the start date as a parameter from the URL 
@app.route("/api/v1.0/<start_date>")

def start_route(start_date):
    #The minimum, average, maximum temperature for a specified start or start-end range
    session = Session(engine)
    
    query_result = session.query(func.min(meas.tobs), func.avg(meas.tobs), func.max(meas.tobs)).\
        filter(meas.date >= start_date).all()
    session.close()

    #For a specified start, calculate minimum, average, maximum temperature for all the dates greater than or equal to the start date.
    start_stats = []
    for tmin, tavg, tmax in query_result:
        start_dict = {}
        start_dict["Min"] = tmin
        start_dict["Average"] = tavg
        start_dict["Max"] = tmax
        start_stats.append(start_dict)

    #If the query returned non-null values return the results, otherwise return an error message
    if start_dict['Min']: 
        return jsonify(start_stats)
    else:
        return jsonify({"error": f"Date {start_date} not found or not formatted as YYYY-MM-DD."}), 404

#Accepts the start & end date as a parameter from the URL  
@app.route("/api/v1.0/<start_date>/<end_date>")

def start_end_route(start_date, end_date):
    
    #JSON list of the minimum, average, maximum temperature for a specified start or start-end range
    session = Session(engine)
    query_result = session.query(func.min(meas.tobs), func.avg(meas.tobs), func.max(meas.tobs)).\
        filter(meas.date >= start_date).filter(meas.date <= end_date).all()
    session.close()

    #Calculate the minimum, average, maximum temperature for the dates from the start date to the end date, inclusive.
    start_end_stats = []
    for Tmin, Tavg, Tmax in query_result:
        start_end_dict = {}
        start_end_dict["Min"] = Tmin
        start_end_dict["Average"] = Tavg
        start_end_dict["Max"] = Tmax
        start_end_stats.append(start_end_dict)

    #If the query returned non-null values return the results, otherwise return an error message
    if start_end_dict['Min']: 
        return jsonify(start_end_stats)
    else:
        return jsonify({"error": f"Date(s) not found, invalid date range or dates not formatted correctly."}), 404

if __name__ == '__main__':
    app.run(debug=True)