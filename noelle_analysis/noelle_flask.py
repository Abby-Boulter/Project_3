#Imports
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data/ERD.sqlite")

#Reflect an existing database into a new model
Base = automap_base()
#Reflect the tables
Base.prepare(autoload_with=engine)

#Save reference to the tables
# ed_visits = Base.classes.ed_visits
# hosp = Base.classes.hospitalizations
# vulnerability = Base.classes.vulnerability
ext_heat_days = Base.classes.extheatdays
ed_visit_35 = Base.classes.ed_visit_35

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/") # no route because this should be homepage
def dashboard():
    session = Session(engine)
    
## visualizations

#################
## Bar charts ##
#################

# HRI data tables have county, year, ed_rate, hosp_rate, vul_rate

    ## query county ed-rates for all years from SQLite database
    results_ed_visit_35 = session.query(ed_visit_35.county, ed_visit_35.year, ed_visit_35.ed_rate).order_by(ed_visit_35.year.asc()).all()

    session.close()

        # Create a dictionary from the row data and append to a list of all_passengers
    all_ed_35 = []
    for county, year, ed_rate in results_ed_visit_35:
        ed_dict = {}
        ed_dict["county"] = county
        ed_dict["year"] = year
        ed_dict["ed_rate"] = ed_rate
        all_ed.append(ed_dict)
    
    return jsonify(all_ed_35)

