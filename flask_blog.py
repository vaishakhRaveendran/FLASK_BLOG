#You should add your flask application to environment variable to run the app else add app.run() at the end
#You also turn on the debugging mode for live server.
from flask import Flask
#creating a instance of flask class in a variable called the app.
app = Flask(__name__)

#Adding the home page
@app.route("/")
#Routes are what we type into browsers to go into different websites
#Route decorators handles all the complicated backend stuff and simply allows us to write a function that returns what is given to the website
#'/' represents the home page of the website
def hello_world():
    return "<h1>Welcome Home Page!</h1>"

#Adding the about page
@app.route("/about")
#The about function will return a html to the about page
def about():
    return "<h1>HURRAY ABOUT PAGE</h1>"
#if you want to add more routers it is simply add more router decorators.


if __name__=='__main__':
    app.run(debug=True)