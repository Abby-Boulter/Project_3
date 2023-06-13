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
ext_heat_days = Base.classes.extreme_heat_days
ed_visit_35 = Base.classes.ed_visit_35

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/aboutus")
def aboutus():
    
    return render_template("aboutus.html")
    

###################################################################
## Bar & line chart querries for extreme heat days and ED visits ##
###################################################################
@app.route("/ehd")
def ehd():
    session = Session(engine)
# Extreme heat days data tables have county, year, ed_rate, hosp_rate, vul_rate

    ## query county ed-rates for all years from SQLite database
    results_ext_heat_days = session.query(ext_heat_days.county, ext_heat_days.year, ext_heat_days.ext_heat_days).order_by(ext_heat_days.year.asc()).all()

        # Create a dictionary from the row data and append to a list of all_passengers
    all_ehd = []
    for county, year, ext_heat_days in results_ext_heat_days:
        ed_dict = {}
        ed_dict["county"] = county
        ed_dict["year"] = year
        ed_dict["ed_rate"] = ext_heat_days
        all_ehd.append(ed_dict)
    
    return jsonify(all_ehd)

    session.close()

    return render_template("ehd.html", all_ehd=all_ehd)

###################################################################

@app.route("/ed35")
def edvisits35():
    session = Session(engine)
# HRI data tables have county, year, ed_rate, hosp_rate, vul_rate

    ## query county ed-rates for all years from SQLite database
    results_ed_visit_35 = session.query(ed_visit_35.county, ed_visit_35.year, ed_visit_35.ed_rate).order_by(ed_visit_35.year.asc()).all()
    
    # Create a dictionary from the row data and append to a list of all_passengers
    all_ed_35 = []
    for county, year, ed_rate in results_ed_visit_35:
        ed_dict = {}
        ed_dict["county"] = county
        ed_dict["year"] = year
        ed_dict["ed_rate"] = ed_rate
        all_ed_35.append(ed_dict)
    
    return jsonify(all_ed_35)
    
    session.close()

    return render_template("ed35.html", all_ed_35=all_ed_35)