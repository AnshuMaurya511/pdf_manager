from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, PasswordField, EmailField
from wtforms.validators import length, Email, EqualTo,DataRequired

class RegistrationForm(FlaskForm):
    fullname = StringField("Fullname", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),length(min=4)])
    confirm = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
