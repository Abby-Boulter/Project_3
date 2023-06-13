import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template 
import numpy as np
import json 
from flask_cors.extension import CORS 
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data/hri.sqlite")

#Reflect an existing database into a new model
Base = automap_base()
#Reflect the tables
Base.prepare(autoload_with=engine)

#Save reference to the table


ed_visit_35 = Base.classes.ed_visit_35

heat_days = Base.classes.extreme_heat_days
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
cors = CORS(app)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
      return render_template("index.html")

@app.route("/edvisit") # no route because this should be homepage
def dashboard():
    session = Session(engine)
    
## visualizations

#################
## Bar charts ##
#################

# HRI data tables have county, year, ed_rate, hosp_rate, vul_rate

    ## query county ed-rates for all years from SQLite database
    results_ed_visit_35 = session.query(ed_visit_35.county, ed_visit_35.year, ed_visit_35.ed_rate_35).order_by(ed_visit_35.year.asc()).all()

    session.close()

        # Create a dictionary from the row data and append to a list of all_passengers
    all_ed_35 = []
    for county, year, ed_rate_35 in results_ed_visit_35:
        ed_dict = {}
        ed_dict["county"] = county
        ed_dict["year"] = year
        ed_dict["value"] = ed_rate_35
        all_ed_35.append(ed_dict)
    
    return jsonify(all_ed_35)

@app.route("/heatdays") # no route because this should be homepage
def heat():
    session = Session(engine)
    global heat_days
    
## visualizations

    ## query county ed-rates for all years from SQLite database
    results_ext_heat_days = session.query(heat_days.county, heat_days.year, heat_days.ext_heat_days).order_by(heat_days.year.asc()).all()

    session.close()

        # Create a dictionary from the row data and append to a list of all_passengers
    all_ext_heat = []
    for county, year, heat_days in results_ext_heat_days:
        ext_dict = {}
        ext_dict["county"] = county
        ext_dict["year"] = year
        ext_dict["value"] = ext_heat_days
        all_ext_heat.append(ext_dict)
    
    return jsonify(all_ext_heat)

@app.route("/countiesjson")
def test():
  with open('data/arizona-with-county-boundaries_1085.geojson','r') as gdata:
    geojson = json.load(gdata)
    print(geojson)
    return geojson



if __name__ == "__main__":
    app.run(debug=True)


