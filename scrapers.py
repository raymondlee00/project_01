import requests


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


def getbackgroundmap(minlat, maxlat, minlong, maxlong):
    app_id = None
    app_code = None
    with open('keys.txt') as file:
        app_id = file.readline()
        app_code= file.readline()
    print(app_id, app_code)



getbackgroundmap(5,5,5,5)

#todo: add scraping of FAA site for callsign, then generate google search from plane make and model, then grab images
