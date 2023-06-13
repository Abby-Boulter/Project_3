import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template 

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data/hri.sqlite")

#Reflect an existing database into a new model
Base = automap_base()
#Reflect the tables
Base.prepare(autoload_with=engine)

#Save reference to the table
#hri = Base.classes.hri
#ed_visit = Base.classes.ed_visit
#hospitalization = Base.classes.hospitalization
#vulnerability = Base.classes.vulnerability
#ed_visit_35 = Base.classes.ed_visit_35

county= Base.classes.county
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

@app.route("/heat")
def heat():
   session = Session(engine)

   results = session.query(county.hri).all()

   session.close()
 


if __name__ == "__main__":
    app.run(debug=True)


