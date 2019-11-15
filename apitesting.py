import json, urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'https://opensky-network.org/api/states/all?lamin=45.8389&lomin=5.9962&lamax=47.8229&lomax=10.5226')
r.data
print(r.data)