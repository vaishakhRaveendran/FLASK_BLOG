from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import  DataRequired,Length,Email,EqualTo

#Registration forms will be created as class which inherits the FlaskForm class.
class RegistrationForm(FlaskForm):
    UserName=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    Email=StringField('Email',validators=[DataRequired(),Email()])
    Password=PasswordField('Password',validators=[DataRequired()])
    Confirm_Password = PasswordField('Confirm_Password', validators=[DataRequired(),EqualTo('Password')])
    Submit=SubmitField('Sign Up')


class LoginForm(FlaskForm):
    Email=StringField('Email',validators=[DataRequired(),Email()])
    Password=PasswordField('Password',validators=[DataRequired()])
    Remember=BooleanField('Remember Me')
    Submit=SubmitField('Sign_In')