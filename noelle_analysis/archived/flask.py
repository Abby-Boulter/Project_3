import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data/hri.sqlite")

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

### Flask Routes

@app.route("/")
def dashboard():
    session = Session(engine)