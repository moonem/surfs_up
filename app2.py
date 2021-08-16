from enum import auto
import flask
import datetime as dt
import numpy as np
import pandas as pd

# add sqlalchemy dependencies
import sqlalchemy
from sqlalchemy import engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import flask dependency
from flask import Flask, jsonify

# Set up the database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes.
Base = automap_base()

# Reflect the table
Base.prepare(engine, reflect=True)

# Create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database 
session = Session(engine)

# Create a new Flask Application calle "app"
app = Flask(__name__)

# Define the starting point also knows as "root"
#@app.route('/')

# Create a function 'hello_world'. Whenever you make a route in Flask, you put the code you want in that specific route below
#def hello_world():
    #return 'Hello world'

@app.route('/')

# Create a function welcome() with a return statement. 
# Add the precipitation, stations, tobs, and temp routes 
# that we'll need for this module into our return statement.
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

    #@app.route("/api/v1.0/precipitation")