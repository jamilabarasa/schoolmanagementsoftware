from config import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String,nullable=False)
    lastname = db.Column(db.String,nullable=False)
    email = db.Column(db.String,nullable=False)
    telephone = db.Column(db.String,nullable=False) 
    dob = db.Column(db.Date,nullable=True)
    teacher = db.Column(db.Boolean,nullable=False,default=False)
    student = db.Column(db.Boolean,nullable=False,default=False)
    admno = db.Column(db.String,nullable=True)
    parent = db.Column(db.Boolean,nullable=False,default=False)
    admin = db.Column(db.Boolean,nullable=False,default=False)
    passwordhash = db.Column(db.String,nullable=False)

    @property
    def password(self):
        raise AttributeError("password is write only")

    def setpassword(self,password):
        self.passwordhash = generate_password_hash(password)

    def verifypassword(self,password):
        return check_password_hash(self.passwordhash,password)     

    def setstudent(self):
        self.student=True

    def setteacher(self):
        self.teacher=True
    
    def setparent(self):
        self.parent=True

    def setadmin(self):
        self.admin=True

    def __repr__(self):
        return "<User {} {}>".format(self.firstname,self.lastname)

class Subject(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)

    def __repr__(self):
        return "<subject %r>" %self.name