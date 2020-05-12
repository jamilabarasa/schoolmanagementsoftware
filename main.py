from config import app, db
from flask import render_template, request, flash, url_for, redirect
from flask_login import LoginManager, login_user
from forms import *
from models import *

# login manager config
login_manager = LoginManager()
login_manager.login_view = 'adminlogin'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_first_request 
def createtables():
    db.create_all()

@app.route('/login/admin',methods=['GET','POST'])
def adminlogin():
    form = Adminlogin()
    if request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.admin:
                if user.verifypassword(form.password.data):
                    login_user(user)
                    return redirect(url_for('admindashboard'))
                else:
                    flash('Invalid credentials')
            else:
                flash("You are not allowed to log in here")
        else:
            flash('User not found')
    return render_template("adminlogin.html",form=form)

@app.route('/admin/dashboard')
def admindashboard():
    return render_template('admindashboard.html')

@app.route('/login/teacher',methods=['GET','POST'])
def teacherlogin():
    form = Adminlogin()
    if request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.teacher:
                if user.verifypassword(form.password.data):
                    login_user(user)
                    return redirect(url_for('teacherdashboard'))
                else:
                    flash('Invalid credentials')
            else:
                flash("You are not allowed to log in here")
        else:
            flash('User not found')
    return render_template("teacherlogin.html",form=form)

@app.route('/teacher/dashboard')
def teacherdashboard():
    return render_template('teacherdashboard.html')

@app.route('/admin/subjects',methods = ['GET','POST']) 
def subjects():
    form = SubjectsForm()
    if request.method=='POST':
        subject = Subject(name=form.name.data)
        db.session.add(subject)
        db.session.commit()
        flash('{} was successfully added'.format(subject.name))
        return redirect(url_for('subjects'))

    return render_template('subjects.html' ,form=form)

if __name__=="__main__":
    app.run(debug=True)