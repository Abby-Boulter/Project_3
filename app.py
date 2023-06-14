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

heat_days = Base.classes.extreme_heat_days
ed_visit_35 = Base.classes.ed_visit_35

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



if __name__ == "__main__":
    app.run(debug=True)





