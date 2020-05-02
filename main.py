from config import app
from flask import render_template
from forms import *

@app.route('/login/admin',methods=['GET','POST'])
def adminlogin():
    form = Adminlogin()
    return render_template("adminlogin.html",form=form)

if __name__=="__main__":
    app.run(debug=True)