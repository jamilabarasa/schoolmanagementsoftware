from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DFFDFDDDSSDSCBNB'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/mila/Desktop/PYTHON/school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)