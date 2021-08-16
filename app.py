# import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# set up our database engine for the Flask application
# The create_engine() function allows us to access and query our SQLite database file.
engine = create_engine("sqlite:///hawaii.sqlite")

# let's reflect the database into our classes
Base = automap_base()

# reflect the database
Base.prepare(engine, reflect=True)

# We'll create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

# Finally, create a session link from Python to our database
session = Session(engine)

# create a new Flask instance/application called "app"
app = Flask(__name__)

# define the starting point, also known as the root. 
# To do this, we'll use the function @app.route('/')
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# For our FLASK_APP environment variable, we want to 
# modify the path that will run our app.py file. Run in command line:
#set FLASK_APP=app.py
#flask run

# create a new route "precipitation"
@app.route("/api/v1.0/precipitation")

# Next, we will create the precipitation() function
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)


# create a new route "stations"
@app.route("/api/v1.0/stations")

# create stations function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results)) # unraveling our results into a one-dimensional array/list
    return jsonify(stations=stations)  # jsonify the list and return it as JSON

# create a new route "tobs"
@app.route("/api/v1.0/tobs")

# create temp_monthly function
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# create new routes to provide both a starting and ending date.
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# create a stats function
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).filter(Measurement.date >= start).all() 
        #asterisk indicates multiple results will be there
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)