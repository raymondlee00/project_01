from flask import Flask, render_template, flash, redirect, url_for, request
from apitesting import planeswithin
from scrapers import location
import pygal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('radius_form.html')


@app.route('/results', methods=[ 'POST'])
def showPlanes():
    latitude = float(request.form.get("latitude"))
    longitude = float(request.form.get("longitude"))
    print(longitude)
    print(latitude)
    myloc = location()
    mylat = float(myloc['latitude'])
    mylong = float(myloc['longitude'])
    planes = planeswithin(mylat - latitude, mylat + latitude, mylong - longitude, mylong + longitude, False)
    print(mylat - latitude, mylat + latitude, mylong - longitude, mylong + longitude)
    chart = pygal.XY(yrange=(mylat - latitude, mylat + latitude), xrange=(mylong - longitude, mylong + longitude))
    chart.title = 'Planes near you'

    for plane in planes:
        try:
            templist = [(float(plane[1]), (float(plane[0])))]
            chart.add('callsign:' + plane[6], templist)
        except:
            print("blank")
    #Todo: your location indicator
    print((mylat, mylong - longitude ), (mylat, mylong + longitude))
    #chart.add('you', [(mylat, mylong - longitude ), (mylat, mylong + longitude )])
    print((mylat - latitude , mylong), (mylat + latitude, mylong))
  #  chart.add('you', [(mylat - latitude, mylong), (mylat + latitude, mylong)])
    chart = chart.render_data_uri()
    return render_template('results.html', planes = planes, chart = chart)
