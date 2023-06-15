import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template 
import numpy as np
import json 
#from flask_cors.extension import CORS
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data/hri.sqlite")

# #Reflect an existing database into a new model
Base = automap_base()
# #Reflect the tables
Base.prepare(autoload_with=engine)

# #Save reference to the table

heat_days = Base.classes.extreme_heat_days
ed_visit_35 = Base.classes.ed_visit_35

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
# cors = CORS(app)
#################################################
# Flask Routes

#################################################

@app.route("/")
def home():
      return render_template("index.html")

#heat days Route
@app.route("/extreme")
def extremeH():
    #Create our session (link) from Python to the DB
    session = Session(engine)

    #Return a list of ED rates and year
    ext_sess  = session.query(heat_days.county, heat_days.year, heat_days.ext_heat_days)

    session.close()

    #Put values into a dictionary to be displayed.
    ext_values = []
    for ct, yr, rt in ext_sess:
        ext_dict = {}
        ext_dict["county"] = ct
        ext_dict["year"] = yr
        ext_dict["ext_heat_days"] = rt
        ext_values.append(ext_dict)

    #display jsonified results
    return jsonify(ext_values) 


# Ed Visit Route
@app.route("/edvisit")
def edVisit():
    #Create our session (link) from Python to the DB
    session = Session(engine)

    #Return a list of ED rates and year
    ed_sess  = session.query(ed_visit_35.county, ed_visit_35.year, ed_visit_35.ed_rate_35)

    session.close()

    #Put values into a dictionary to be displayed.
    ed_values = []
    for ct, yr, rt in ed_sess:
        ed_dict = {}
        ed_dict["county"] = ct
        ed_dict["year"] = yr
        ed_dict["ext_heat_days"] = rt
        ed_values.append(ed_dict)

    #display jsonified results
    return jsonify(ed_values) 


if __name__ == "__main__":
    app.run(debug=True)





