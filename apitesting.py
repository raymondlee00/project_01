import json, urllib3, requests, math, pygal
from opensky_api import OpenSkyApi



#opensky stuff goes here
def planeswithin(minlat, maxlat, minlong, maxlong):
    api = OpenSkyApi()
    states = api.get_states(bbox=(minlat, maxlat, minlong, maxlong))
    holdout = []
    for s in states.states:
        holdout.append("(%r, %r, %r, %r)" % (s.longitude, s.latitude, s.baro_altitude, s.velocity))
    return(holdout)

#geolocation stuff goes here
def location():
    ip_grabber = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_grabber.json()['ip']
    reqbuilder = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
    loc_req = requests.get(reqbuilder)
    loc_data = loc_req.json()
    return(loc_data)

#todo: math to make this radius
def planes_near_me(radius):
    myloc = location()

    #planeswithin()

def pointfrompoint(d, heading, lat1 = float(location()['latitude']), lon1 = float(location()['longitude'])):
    # lat = math.asin(math.sin(lat1) * math.cos(d) + math.cos(lat1) * math.sin(d) * math.cos(heading))
    #
    # lon = (lon1 - math.asin(math.sin(heading) * math.sin(d) / math.cos(lat)) + math.pi)%(2 * math.pi) - math.pi
    #
    lat = math.asin(math.sin(lat1) * math.cos(d) + math.cos(lat1) * math.sin(d) * math.cos(heading))
    dlon = math.atan2(math.sin(heading) * math.sin(d) * math.cos(lat1), math.cos(d) - math.sin(lat1) * math.sin(lat))
    lon = (lon1 - dlon + math.pi)%( 2 * math.pi) - math.pi
    print(lat, lon)


print(location())
pointfrompoint(3,math.pi)
planes_near_me(5)


# 40.7263 + -0.2559971502571034
# -73.9818 + 1.4164236861550314
#
#         40.4703028497429,-72.56537631384498