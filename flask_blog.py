from flask import Flask, render_template,url_for

# Creating an instance of the Flask class and storing it in a variable called 'app'.
app = Flask(__name__)

# Imagine we made a database call and got this list, and now we want to pass it to the website.
# We can do this by passing 'posts' as an argument to the 'posts' variable in render_template,
# and then we can access it in the HTML page.

posts = [
    {
        'Author': 'Vaishakh M',
        'Title': 'My Blog Page',
        'Content': 'Cross Validation',
        'Date': '28-10-23'
    },
   {
        'Author': 'Raveendran P V',
        'Title': 'Fitness',
        'Content': 'Yoga For Health',
        'Date': '18-10-23'
    },
    {
        'Author': 'Lakshmi M',
        'Title': 'Tutorial Page',
        'Content': 'Feature Engineering',
        'Date': '28-03-23'
    }
]

# Adding the home page
@app.route("/")
# Route decorators handle all the backend functionality, allowing us to define a function that returns content for the website.
def hello_world():
    return render_template('home.html', posts=posts)

# Adding the about page
@app.route("/about")
# The 'about' function returns an HTML page for the 'about' page.
def about():
    return render_template('about.html')

# If you want to add more routes, simply add more route decorators.

if __name__ == '__main__':
    app.run(debug=True)
