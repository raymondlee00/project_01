from flask import Flask, render_template, flash, redirect, url_for, request
from wtforms import Form
from apitesting import planeswithin,

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    render_template('radius_form.html')


@app.route('/results', methods=['GET', 'POST'])
def showPlanes():
    radius = request.form.get('radius')
