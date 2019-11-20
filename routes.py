from flask import Flask, render_template, flash, redirect, url_for, request, session
import os #for generating a secret key
from apitesting import planeswithin
from scrapers import location,getmap
import pygal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utl import db_ops

app = Flask(__name__)

#Secret key handling
secret_key_file = 'secret_key.txt'
if (os.path.exists(secret_key_file)): #check if secret key file already exists
    file = open(secret_key_file, 'r')
    app.secret_key = file.read()
else: #not adding the secret key file, so generate one on the spot for ppl without it
    file = open(secret_key_file, 'w+') #w+ creates the file if it doesn't exist
    file.write(str(os.urandom(32)))
    app.secret_key = file.read()

file.close()

# if logged in: welcome page, else login page
@app.route("/", methods=['GET', 'POST'])
def home():
    if 'user' in session: #checks that a user is logged into a session, render welcome page
        #print("Session username: " + session['user'])
        flash ("You are logged in.")
        print(session['user'])
        return render_template("base.html", username = str(session['user']))

    return render_template("login.html") #if not, then render login page

# login page
@app.route("/auth", methods=['POST'])
def login():
    username = request.form.get('user')
    password = request.form.get('pw')

    if (db_ops.authenticate(username, password)):
        session['user'] = username
        return redirect(url_for('home')) #should trigger if statement in "/" route

    flash("Failed to log in. The username or password provided did not match any accounts.")
    return redirect(url_for('home'))

# signup route redirects to the register page template
@app.route("/signup")
def signup():
    return render_template("register.html")

# register for a new account page
@app.route("/register", methods=['POST'])
def register():
    username = request.form.get('user')
    password = request.form.get('pw')

    if (db_ops.accountExists(username)):
        flash("This username is already in use. Try another one.")
        return redirect(url_for('signup'))

    db_ops.addAccount(username, password)
    flash("You have successfully created your account. Please log in now.")
    return redirect(url_for('home'))

# logout page
@app.route("/logout")
def logout():
    if 'user' in session: #checks that a user is logged into a session
        session.pop('user') #logs the user out of the session
        flash("You have been logged out.")
        return redirect(url_for('home'))

    flash("You are already logged out.")
    return redirect(url_for('home'))

@app.route('/results', methods=['GET', 'POST']) # somehow get works but post doesn't ;(
def showPlanes():
    if 'user' in session: #checks that a user is logged into a session
        latitude = float(request.form.get("latitude"))
        longitude = float(request.form.get("longitude"))
        print(longitude)
        print(latitude)
        myloc = location()
        mylat = float(myloc['latitude'])
        mylong = float(myloc['longitude'])
        planes = planeswithin(mylat - latitude, mylat + latitude, mylong - longitude, mylong + longitude, False)
        print(mylat - latitude, mylat + latitude, mylong - longitude, mylong + longitude)
       # getmap(mylat,mylong,planes)
        return render_template('results.html',  map = getmap(mylat,mylong,planes))
    flash("You must log in first before you can view the results!")
    return redirect(url_for('home'))

@app.route('/radiusform', methods=['GET', 'POST'])
def radiusForm():
    if 'user' in session: #checks that a user is logged into a session
        return render_template("radius_form.html")
    flash("You must log in first before you can access the radius form!")
    return redirect(url_for('home'))

if __name__  == "__main__":
        app.debug = True
        app.run()