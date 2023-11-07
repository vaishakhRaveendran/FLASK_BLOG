from flask import Flask, render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY']='c2bbbe4aa84532a255b3dde019dcbdb8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#Secret Keys are required to protect the website from attacks.
# Creating an instance of the Flask class and storing it in a variable called 'app'.
db = SQLAlchemy(app)
app.app_context().push()

#Using sqlAlchemy we can represent the databases as classes.
#Creating user class for holding the user data
#Users and posts will be having a one to many relationship
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    posts=db.relationship('Post',backref='author',lazy=True)
    #posts column in user will run a additional query to get all the post created by the user.

    def __repr__(self):
        return f'User: {self.username},{self.email}'

#Creating a post class for creating and maintaing blog posts

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    datePosted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f'User: {self.title},{self.datePosted}'



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
def home():
    return render_template('home.html', posts=posts)

# Adding the about page
@app.route("/about")
# The 'about' function returns an HTML page for the 'about' page.
def about():
    return render_template('about.html')

# If you want to add more routes, simply add more route decorators.
#We should allow routes to accept messages from post methods to accept the datas.
@app.route("/register",methods=['GET','POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():#You are validation your form
        flash(f'Account created for {form.UserName.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Sign_Up',form=form)

@app.route("/login")
def login():
    form=LoginForm()
    return render_template('login.html',title='Login_In',form=form)

if __name__ == '__main__':
    app.run(debug=True)
