import os
import numpy as np
from datetime import datetime as dt
from flask import (
    Flask, 
    render_template, 
    jsonify,
    request, 
    redirect,
    url_for)
from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/gooddeeds.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
today=dt.today()
mydate=""


class GoodDeedsSignUp(db.Model):
    __tablename__ = 'goodeedsign'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(64))
    lname = db.Column(db.String(64))
    myemail = db.Column(db.String(64))
    password1 = db.Column(db.String(64))
    password2 = db.Column(db.String(64))
    mydate=db.Column(db.String(24))
    def __repr__(self):
        return '<GoodDeedsSignUp %r>' % (self.name)

@app.before_first_request
def setup():     # Recreate database each time for demo
    #db.drop_all()
    db.create_all()
#################################################
# Routes
#################################################

@app.route('/')
def index():
    files=[]
    files = ['static/assets/JourneyofKindness.jpg' ]
    return render_template('index.html', usfiles = files)

@app.route('/mydata', methods=['GET', 'POST'])
def mydata():
    if request.method == 'POST':
        today=dt.today()
        fname=request.form['fname'];
        lname=request.form['lname'];
        myemail=request.form['email'];
        password1=request.form['psw'];
        password2=request.form['pswrepeat'];
        mydate=dt.strftime(today, "%m-%d-%Y\n%I:%M:%S");

        goodeed=GoodDeedsSignUp(fname=fname, lname=lname, myemail=myemail, password1=password1, password2=password2, mydate=mydate)
        db.session.add(goodeed)
        db.session.commit()
        return redirect('/su', code=302)

@app.route("/mission", methods=['GET', 'POST'])
def mission():
    files= [ 'static/assets/ImagineLg.jpg' ]
    return render_template('mission.html', usfiles=files)

@app.route("/cert", methods=['GET', 'POST'])
def certAwe():
    files= ['static/assets/Awesomeness.jpg', 'static/assets/Awesomeness.pdf']
    return render_template('certAwesome.html', usfiles=files)

@app.route("/didIoffer", methods=['GET', 'POST'])
def diof():
    files= ['static/assets/DidIOffer.jpg', 'static/assets/BeThatOne.jpg', 'static/assets/SomeGoodDeeds.jpg', 'static/assets/Imagine.jpg', 'static/assets/KindnessCan.jpg','static/assets/NOWHERE.jpg']
    return render_template('didIoffer.html', usfiles=files)

@app.route("/didIoffer2", methods=['GET', 'POST'])
def diof2():
    files= ['static/assets/FocusOnTheGood.jpg', 'static/assets/FocusOnTheGood2.jpg', 'static/assets/BeTheChange.jpg', 'static/assets/DreamKindness.jpg', 'static/assets/GratitudeFriends.jpg','static/assets/TrueFriend.jpg']
    return render_template('didIoffer2.html', usfiles=files)


@app.route("/speech", methods=['GET', 'POST'])
def speech():
    return render_template('speech.html', list=[])

@app.route("/gdlinks", methods=['GET', 'POST'])
def gdlinks():
    files= [ 'static/assets/Imagine.jpg' ]
    return render_template('gdlinks.html', usfiles=files)

@app.route("/batam", methods=['GET', 'POST'])
def batam():
    return render_template('buddhaangryman.html', list=[])

@app.route("/farm", methods=['GET', 'POST'])
def farm():
    return render_template('missPutPut.html', list=[])

@app.route("/t2wolves", methods=['GET', 'POST'])
def t2wolves():
    return render_template('the2wolves.html', list=[])

@app.route("/tstarfish", methods=['GET', 'POST'])
def tstarfish():
    return render_template('theStarfishStory.html', list=[])

@app.route("/su", methods=['GET', 'POST'])
def signup():
    files = ['static/assets/BeThatOne.jpg', 'static/assets/SomeGoodDeeds.jpg', 'static/assets/JourneyofKindness.jpg', 'static/assets/Imagine.jpg', 'static/assets/NOWHERE.jpg']
    return render_template('signUp.html', usfiles=files)

@app.route("/tpc1", methods=['GET', 'POST'])
def phone1():
    return render_template('thePhoneCallpg1.html', list=[])

@app.route("/tpc2", methods=['GET', 'POST'])
def phone2():
    return render_template('thePhoneCallpg2.html', list=[])

@app.route("/tpc3", methods=['GET', 'POST'])
def phone3():
    return render_template('thePhoneCallpg3.html', list=[])

@app.route("/poem1", methods=['GET', 'POST'])
def poem1():
    return render_template('magicMirrorKindness.html', list=[])

@app.route("/poem2", methods=['GET', 'POST'])
def poem2():
    return render_template('whatIsLifeFor.html', list=[])

@app.route("/poem3", methods=['GET', 'POST'])
def poem3():
    return render_template('lightBulbMoments.html', list=[])

@app.route("/gdmaillist", methods=['GET', 'POST'])
def list_goodeeds():
    results = db.session.query(GoodDeedsSignUp.fname, GoodDeedsSignUp.lname, GoodDeedsSignUp.myemail, GoodDeedsSignUp.password1, GoodDeedsSignUp.password2, GoodDeedsSignUp.mydate).all()

    gooddeeds = []
    for result in results:
        gooddeeds.append({
            "fname": result[0],
            "lname": result[1],
            "myemail": result[2],
            "password1": result[3],
            "password2": result[4],
            "mydate":result[5]
        })
    return render_template('result.html', gooddeeds=gooddeeds)


if __name__ == "__main__":
    app.run(debug=True)
