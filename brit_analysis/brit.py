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

app = Flask(__name__)
cors = CORS(app)

engine = create_engine("sqlite:///..data/HRI.sqlite")
Base = automap_base()
#Reflect the tables
Base.prepare(autoload_with=engine)
ed_visit_35 = Base.classes.ed_visit_35


@app.route("/")
def return_data():
     result=engine.execute('select * from data').fetchall()
     




      


# @app.route("/")
# def home():
#       return render_template("first.html")



if __name__ == "__main__":
    app.run(debug=True)





