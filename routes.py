from flask import Flask, render_template, flash, redirect, url_for, request
from apitesting import planeswithin, location
import pygal
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
    chart = pygal.XY(xrange=(mylat - latitude, mylat + latitude), yrange=(mylong - longitude, mylong + longitude))
    chart.title = 'Planes near you'
    for plane in planes:
        try:
            templist = [(float(plane[0]), -(float(plane[1])))]
            chart.add('callsign:' + plane[6], templist)
        except:
            print("blank")
    chart = chart.render_data_uri()
    return render_template('results.html', planes = planes, chart = chart)
