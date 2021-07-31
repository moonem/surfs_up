import flask


# pip install flask

# Import flask dependency
from flask import Flask

# Create a new Flask App instance
app = Flask(__name__)

# Define the starting point also knows as "root"
@app.route('/')

# Create a function 'hello_world'. Whenever you make a route in Flask, you put the code you want in that specific route below
def hello_world():
    return 'Hello world'

# Modify the path that will run our app.py file so that we can run our file
#