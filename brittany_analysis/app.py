import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template 

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data/ERD.sqlite")

# # reflect an existing database into a new model
Base = automap_base()
# # reflect the tables
Base.prepare(autoload_with=engine)

# # Save reference to the table
County= Base.classes.county

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def dashboard():
 
    #Create our dashboard
    
    #session = Session(engine)
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)