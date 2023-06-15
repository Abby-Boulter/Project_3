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







df = data.js().query("city=Arizona'")
fig = px.line(df, x="year", y="rate", color='county')
fig.show()




app.layout = html.Div([
  html.H4('ED Visits '),
  dcc.Graph(id="graph"),
  dcc.Checklist(
      id="checklist",
      options=["Counties, Arizona, Pima"],
      value=["visits"],
      inline=True
  ),
])

app = Flask(__name__)
app.config["DEBUG"] = True

cors = CORS(app)

@app.callback(
  Output("graph", "figure"), 
  Input("checklist", "value"))
def update_line_chart(counties):
  df = data.js() #
  mask = df.county.isin(counties)
  fig = px.line(df[mask], 
      x="year", y="rate", color='county')
  return fig


app.run_server(debug=True)
    




     






      


# @app.route("/")
# def home():
#       return render_template("index.html")



if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)






