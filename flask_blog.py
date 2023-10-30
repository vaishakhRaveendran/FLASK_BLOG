from flask import Flask
#creating a instance of flask class in a variable called the app.
app = Flask(__name__)
@app.route("/")
#Routes are what we type into browsers to go into different websites
#Route decorators handles all the complicated backend stuff and simply allows us to write a function that returns what is given to the website
#'/' represents the home page of the website
def hello_world():
    return "<p>Hello, World!</p>"