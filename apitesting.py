import json, urllib3, requests, math, pygal
from opensky_api import OpenSkyApi


# opensky stuff goes here
def planeswithin(minlat, maxlat, minlong, maxlong):
    api = OpenSkyApi()
    states = api.get_states(bbox=(minlat, maxlat, minlong, maxlong))
    holdout = []
    for s in states.states:
        holdout.append("(%r, %r, %r, %r, %r, %r, %r)" % (
        s.longitude, s.latitude, s.baro_altitude, s.velocity, s.heading, s.icao24, s.callsign))
    return (holdout)


# geolocation stuff goes here
# todo:reconnect this when finished testing
def location():
    try:
        ip_grabber = requests.get('https://get.geojs.io/v1/ip.json')
        my_ip = ip_grabber.json()['ip']
        reqbuilder = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
        loc_req = requests.get(reqbuilder)
        loc_data = loc_req.json()
    except:
        loc_data = {'longitude': '-73.9267', 'city': 'Brooklyn', 'timezone': 'America/New_York', 'accuracy': 20,
                    'asn': 21704, 'region': 'New York', 'organization_name': 'New York City Board of Education',
                    'organization': 'AS21704 New York City Board of Education', 'country_code': 'US',
                    'ip': '165.155.140.163', 'latitude': '40.6877', 'area_code': '0', 'continent_code': 'NA',
                    'country': 'United States', 'country_code3': 'USA'}

    return (loc_data)


# todo: math to make this radius

def planes_near_me(latitude, longitude):
    myloc = location()
    mylat = float(myloc['latitude'])
    mylong = float(myloc['longitude'])
    return planeswithin(mylat - latitude, mylat + latitude, mylong - longitude, mylong + longitude)

    # planeswithin()


def pointfrompoint(d, heading, lat1=float(location()['latitude']), lon1=float(location()['longitude'])):
    # lat = math.asin(math.sin(lat1) * math.cos(d) + math.cos(lat1) * math.sin(d) * math.cos(heading))
    #
    # lon = (lon1 - math.asin(math.sin(heading) * math.sin(d) / math.cos(lat)) + math.pi)%(2 * math.pi) - math.pi
    #
    lat = math.asin(math.sin(lat1) * math.cos(d) + math.cos(lat1) * math.sin(d) * math.cos(heading))
    dlon = math.atan2(math.sin(heading) * math.sin(d) * math.cos(lat1), math.cos(d) - math.sin(lat1) * math.sin(lat))
    lon = (lon1 - dlon + math.pi) % (2 * math.pi) - math.pi
    print(lat, lon)


#print(location())
# pointfrompoint(3,math.pi)


# 40.7263 + -0.2559971502571034
# -73.9818 + 1.4164236861550314
#
#         40.4703028497429,-72.56537631384498
