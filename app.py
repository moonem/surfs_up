# import dependencies
from flask import Flask

# create a new Flask instance called app
app = Flask(__name__)

# define the starting point, also known as the root. 
# To do this, we'll use the function @app.route('/')
@app.route('/')
def hello_world():
    return 'Hello world'

# For our FLASK_APP environment variable, we want to 
# modify the path that will run our app.py file
#export FLASK_APP=app.py