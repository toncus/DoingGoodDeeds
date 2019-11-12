import os
import pandas as pd
import numpy as np
import random
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
if os.environ.get('MONGODB_URI'):
    MONGODB_URI=os.environ.get('MONGODB_URI')

app.config["MONGO_URI"] = MONGODB_URI
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
        today=dt.today()
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
        return render_template('thankyou.html', fname=fname)

@app.route('/mygooddeed', methods=['GET', 'POST'])
def mygooddeed():
        files = ['static/assets/AwesomeBorder.jpg']
        my_csv = os.path.join('Resources/Gooddeeds.csv')
        with open(my_csv, newline="") as csvfile:
            mycsv_df = pd.read_csv(my_csv, delimiter=",", encoding='utf-8', header=None)
            pd.set_option('display.max_colwidth', -1)
            mydeed=str(mycsv_df.iloc[int(random.randrange(1,221))])
            mydeed=mydeed[3:-25]
            return render_template('gdsRoulette.html', mydeed=mydeed, usfiles=files)

   
@app.route("/mission", methods=['GET', 'POST'])
def mission():
    files= [ 'static/assets/ImagineLg.jpg' ]
    return render_template('mission.html', usfiles=files)

@app.route("/media", methods=['GET', 'POST'])
def media():
    files= [ 'static/assets/ImagineLg.jpg' ]
    return render_template('media.html', usfiles=files)

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
    files= ['static/assets/BeingGrateful.jpg', 'static/assets/BEYOUTYFULL.jpg', 'static/assets/ThisLittleLight.jpg', 'static/assets/BearHug.jpg', 'static/assets/Imagine4x4.jpg', 'static/assets/KindnessFruits.jpg' ]
    return render_template('didIoffer3.html', usfiles=files)

@app.route("/boot", methods=['GET', 'POST'])
def boot():
    return render_template('bootstrap.html', list=[])

@app.route("/speech", methods=['GET', 'POST'])
def speech():
    return render_template('speech.html', list=[])

@app.route("/gdvids", methods=['GET', 'POST'])
def gdvids():
    return render_template('videos.html', list=[])

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
    files = ['static/assets/AwesomeBorder.jpg']
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

@app.route("/links", methods=['GET', 'POST'])
def links():
    files= ['static/assets/GOODDEEDS.jpg' ]
    return render_template('links.html', usfiles=files)

if __name__ == "__main__":
    app.run(debug=True)