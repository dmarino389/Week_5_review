# This imports all the necessary imports for your form field to work. I will use this setup for all my future forms.
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

# These is my login form setup. It will take a username password a remember me checkbox and a submit field
class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')

# This is my registration form layout
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()]) # This extra Email after datarequired ensures that the email must be done in an email format. To use this I will need to pip install email-validator
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField(
       'Repeat Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
       user = User.query.filter_by(username = username.data).first()
       if user is not None:
          raise ValidationError('Please use a different username')
       

    def validate_email(self, email):
       user = User.query.filter_by(email = email.data).first()
       if user is not None:
          raise ValidationError('Please use a different email adress')
       
  