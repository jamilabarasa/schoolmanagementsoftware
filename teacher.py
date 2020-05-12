from config import app
from flask import render_template, request, flash, url_for, redirect
from flask_login import LoginManager, login_user
from forms2 import *
from models import *

# login manager config
login_manager = LoginManager()
login_manager.login_view = 'teacherlogin'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login/teacher',methods=['GET','POST'])
def teacherlogin():
    form = Teacherlogin()
    if request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.admin:
                if user.verifypassword(form.password.data):
                    login_user(user)
                    return redirect(url_for('loggedin'))
                else:
                    flash('Invalid credentials')
            else:
                flash("You are not allowed to log in here")
        else:
            flash('User not found')
    return render_template("teacherlogin.html",form=form)

@app.route('/loggedin')
def loggedin():
    return "Logged in"

if __name__=="__main__":
    app.run(debug=True)