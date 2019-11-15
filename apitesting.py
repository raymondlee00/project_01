import json, urllib3, requests
from opensky_api import OpenSkyApi



#opensky stuff goes here
http = urllib3.PoolManager()
#r = http.request('GET', 'https://opensky-network.org/api/states/all?lamin=45.8389&lomin=5.9962&lamax=47.8229&lomax=10.5226')
# r.data
# print(r.data)





def planeswithin(minlat, maxlat, minlong, maxlong):
    api = OpenSkyApi()
    states = api.get_states(bbox=(minlat, maxlat, minlong, maxlong))
    for s in states.states:
        print("(%r, %r, %r, %r)" % (s.longitude, s.latitude, s.baro_altitude, s.velocity))






#geolocation stuff goes here



def location():
    ip_grabber = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_grabber.json()['ip']
    reqbuilder = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
    loc_req = requests.get(reqbuilder)
    loc_data = loc_req.json()
    return(loc_data)

