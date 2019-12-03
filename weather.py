import requests
url = 'https://api.airvisual.com/v2/nearest_city?lat={lattitude}&lon={longitude}&key=8e46dfa7-59e4-4a4c-81d2-8872a0eb6cce'
payload = {}
headers = {}
response = requests.request('GET', url.format(lattitude=35.7,longitude=139.6), headers = headers, data = payload, allow_redirects=False)
print(response.text)
