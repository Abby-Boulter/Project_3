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
engine = create_engine("sqlite:///hri.sqlite")
Base = automap_base()
#Reflect the tables
Base.prepare(autoload_with=engine)
ed_visit_35 = Base.classes.ed_visit_35




app = Flask(__name__, static_url_path='',
            static_folder='plot.js',
            template_folder='index.html')
app.config["DEBUG"] = True

cors = CORS(app)



@app.route("/ed") 
def dashboard():
    session = Session(engine)
    

    results_ed_visit_35 = session.query(ed_visit_35.county, ed_visit_35.year, ed_visit_35.ed_rate_35).order_by(ed_visit_35.year.asc()).all()


    all_ed_35 = []
    for county, year, ed_rate_35 in results_ed_visit_35:
        ed_dict = {}
        ed_dict["county"] = county
        ed_dict["year"] = year
        ed_dict["value"] = ed_rate_35
        all_ed_35.append(ed_dict)

    session.close()
    return ("plot.js")
    




     






      


# @app.route("/")
# def home():
#       return render_template("index.html")



if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)






