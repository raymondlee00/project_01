import requests
from apitesting import planeswithin
import csv
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# geolocation stuff goes here
# todo:reconnect this when finished testing
def location():
    try:
        ip_grabber = requests.get('https://get.geojs.io/v1/ip.json')
        my_ip = ip_grabber.json()['ip']
        reqbuilder = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
        loc_req = requests.get(reqbuilder)
        loc_data = loc_req.json()
    except: #todo: make it so that failover data is stored in databse
        loc_data = {'longitude': '-73.9267', 'city': 'Brooklyn', 'timezone': 'America/New_York', 'accuracy': 20,
                    'asn': 21704, 'region': 'New York', 'organization_name': 'New York City Board of Education',
                    'organization': 'AS21704 New York City Board of Education', 'country_code': 'US',
                    'ip': '165.155.140.163', 'latitude': '40.6877', 'area_code': '0', 'continent_code': 'NA',
                    'country': 'United States', 'country_code3': 'USA'}

    return (loc_data)

#todo: make system to check if too many points, and auto retry with lower amount
def getmap(minlat, maxlat, minlong, maxlong, mylat, mylong,planes):
    app_id = None
    app_code = None
    with open('keys.txt') as file:
        app_id = file.readline()
        app_code= file.readline()
    reqbuilder = "https://image.maps.api.here.com/mia/1.6/mapview?"
    #reqbuilder += ("bbox=" + str(maxlat) + "%2C" + str(maxlong) + "%2C" + str(minlat) + "%2C" + str(minlong) + "&")
    reqbuilder += ("w=700&h=800&")
    reqbuilder += ("c=" + str(mylat) + "%2C" + str(mylong) + "&")
    reqbuilder += ("u=" + str(1000) + "&")
    reqbuilder += "poi="
    for idx, i in enumerate(planes):
      #  reqbuilder += "poix" + str(idx) + "=" + i[6] + "%2C" + i[5] + "%3B" + "ffffff" + "%3B" + "ffa500" + "%3B" + str(20) + "%3B" + str(idx) + "&"
        if(idx < len(planes) -1):
            reqbuilder += i[6] + "%2C" + i[5] + "%2C"
        else:
            reqbuilder += i[6] + "%2C" + i[5]

    reqbuilder += "&"
    reqbuilder += "app_id=" + app_id[:-1] + "&app_code=" + app_code
    return(reqbuilder)




#print(getmap(40.6263, -73.9818, planeswithin(39.7263, 41.7263, -74.9818, -72.9818)))

#todo: add scraping of FAA site for callsign, then generate google search from plane make and model, then grab images
def downloadmap(minlat, maxlat, minlong, maxlong, mylat, mylong):
    app_id = None
    app_code = None
    with open('keys.txt') as file:
        app_id = file.readline()
        app_code= file.readline()
    reqbuilder = "https://image.maps.api.here.com/mia/1.6/mapview?"
    reqbuilder += ("bbox=" + str(maxlat) + "%2C" + str(maxlong) + "%2C" + str(minlat) + "%2C" + str(minlong) + "&")
    reqbuilder += ("w=700&h=800&")
    reqbuilder += ("c=" + str(mylat) + "%2C" + str(mylong) + "&")
    reqbuilder += ("u=" + str(1000) + "&")
    reqbuilder += "&"
    reqbuilder += "app_id=" + app_id[:-1] + "&app_code=" + app_code
    imghold = requests.get(reqbuilder, allow_redirects=True)
    open('map.jpeg', 'wb').write(imghold.content)



def graphmaker(minlat, maxlat, minlong, maxlong, mylat, mylong, planes):
    holdplanes = planeswithin(39.7263, 41.7263, -74.9818, -72.9818)
    with open("temp.txt", mode="w+") as file:
        fieldnames = ['latitude', 'longitude']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for plane in holdplanes:
            writer.writerow({'latitude': plane[6], 'longitude': plane[5]})
    df = pd.read_csv('temp.txt')
    df.head()
    BBox = (df.longitude.min(),   df.longitude.max(), df.latitude.min(), df.latitude.max())
    downloadmap(minlat, maxlat, minlong, maxlong, mylat, mylong)
    magic = plt.imread("map.jpeg")
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.scatter(df.longitude, df.latitude, zorder=1, alpha=0.2, c='b', s=10)
    ax.set_title('Plotting Spatial Data on your Map')
    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])
    ax.imshow(magic, zorder=0, extent=BBox, aspect='equal')
    fig.savefig('pointmap.png')
#graphmaker(39.7263, 41.7263, -74.9818, -72.9818, 40.6263, -73.9818, planeswithin(39.7263, 41.7263, -74.9818, -72.9818))

# takes in an array of all the plane states and return an array of 
def generateLatLngArr(statesArr):
    latlngArr = []
    for state in statesArr:
        arr = [0, 0]
        arr[0] = float(state[6])
        arr[1] = float(state[5])
        latlngArr.append(arr)
    return latlngArr


