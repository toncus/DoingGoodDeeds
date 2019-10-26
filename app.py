import os
import numpy as np
import pymongo
from datetime import datetime as dt
from datetime import timedelta as dtd
from flask import (
    Flask, 
    render_template, 
    jsonify,
    request, 
    redirect,
    url_for)
from flask_pymongo import PyMongo

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

app.config["MONGO_DBNAME"] ="gooddeeds"
app.config["MONGO_URI"] = "mongodb://toncus2000:goodeeds5491@ds059205.mlab.com:59205/gooddeeds?retryWrites=false"
mongo = PyMongo(app)

#################################################
# Routes
#################################################

@app.route('/')
def index():
    files=[]
    files = files = ['static/assets/JourneyofKindness.jpg' ]
    return render_template('index.html', usfiles = files)

@app.route('/mydata', methods=['GET', 'POST'])
def mydata():
    if request.method == 'POST':
        today=dt.today()-dtd(hours=4) #randomgiberash
        fname=request.form['fname'];
        lname=request.form['lname'];
        myemail=request.form['email'];
        password1=request.form['psw'];
        password2=request.form['pswrepeat'];
        mydate=dt.strftime(today, "%m-%d-%Y  %I:%M:%S");
        goodeed=mongo.db.goodeedsign
        goodeed.insert({
            'fname':fname, 
            'lname':lname, 
            'myemail':myemail, 
            'password1':password1, 
            'password2':password2, 
            'mydate':mydate}
            )
        return redirect("/su", code=302)
   
@app.route("/gdmaillist", methods=['GET', 'POST'])
def list_goodeeds():
        gooddeeds=[]
        results=mongo.db.goodeedsign.find()
        for result in results:
            fname=result['fname']
            lname=result['lname']
            myemail=result['myemail']
            password1=result['password1']
            password2=result['password2']
            mydate=result['mydate']
            gooddeeds.append({
                'fname':fname, 
                'lname':lname, 
                'myemail':myemail, 
                'password1':password1, 
                'password2':password2, 
                'mydate':mydate})            
        
        
        return render_template('result.html', gooddeeds=gooddeeds)

@app.route("/mission", methods=['GET', 'POST'])
def mission():
    files= [ 'static/assets/ImagineLg.jpg' ]
    return render_template('mission.html', usfiles=files)

@app.route("/cert", methods=['GET', 'POST'])
def certAwe():
    files= ['static/assets/Awesomeness.jpg', 'static/assets/Awesomeness.pdf']
    return render_template('certAwesome.html', usfiles=files)

@app.route("/award", methods=['GET', 'POST'])
def awePers():
    files= ['static/assets/AwesomePersonAward.jpg',]
    return render_template('awardCerts.html', usfiles=files)

@app.route("/didIoffer", methods=['GET', 'POST'])
def diof():
    files= ['static/assets/DidIOffer.jpg', 'static/assets/BeThatOne.jpg', 'static/assets/SomeGoodDeeds.jpg', 'static/assets/Imagine4x4.jpg', 'static/assets/KindnessCan.jpg','static/assets/NOWHERE.jpg']
    return render_template('didIoffer.html', usfiles=files)

@app.route("/didIoffer2", methods=['GET', 'POST'])
def diof2():
    files= ['static/assets/FocusOnTheGood.jpg', 'static/assets/FocusOnTheGood2.jpg', 'static/assets/BeTheChange.jpg', 'static/assets/DreamKindness.jpg', 'static/assets/GratitudeFriends.jpg','static/assets/TrueFriend.jpg']
    return render_template('didIoffer2.html', usfiles=files)

@app.route("/didIoffer3", methods=['GET', 'POST'])
def diof3():
    files= ['static/assets/Imagine4x4.jpg', 'static/assets/JourneyofKindnessCollage.jpg', 'static/assets/ThisLittleLight.jpg', 'static/assets/BearHug.jpg', 'static/assets/KindnessFruits.jpg' ]
    return render_template('didIoffer3.html', usfiles=files)

@app.route("/boot", methods=['GET', 'POST'])
def boot():
    return render_template('bootstrap.html', list=[])

@app.route("/speech", methods=['GET', 'POST'])
def speech():
    return render_template('speech.html', list=[])

@app.route("/gdlinks", methods=['GET', 'POST'])
def gdlinks():
    return render_template('links.html', list=[])

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

if __name__ == "__main__":
    app.run(debug=True)