import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template 
import numpy as np
import json 
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data/hri.sqlite")

#Reflect an existing database into a new model
Base = automap_base()
#Reflect the tables
Base.prepare(autoload_with=engine)

#Save reference to the table

ext_heat_days = Base.classes.extreme_heat_days
ed_visit_35 = Base.classes.ed_visit_35

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

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
        ed_dict["ed_rate"] = ed_rate_35
        all_ed_35.append(ed_dict)
    
    return jsonify(all_ed_35)

@app.route("/countiesjson")
def test():
  with open('data/arizona-with-county-boundaries_1085.geojson','r') as gdata:
    geojson = json.load(gdata)
    print(geojson)
    return geojson



if __name__ == "__main__":
    app.run(debug=True)


