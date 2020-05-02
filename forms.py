from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Email

class Adminlogin(FlaskForm):
    email = StringField('Email',validators=[Email(),DataRequired(),])
    password = PasswordField('Password',validators=[DataRequired(),])
    