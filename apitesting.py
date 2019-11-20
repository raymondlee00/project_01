import json, requests, math, pygal



# opensky stuff goes here

def planeswithin(minlat, maxlat, minlong, maxlong, test = False):
    if not(test):
        restreq = requests.get("https://opensky-network.org/api/states/all?lamin=" +  str(minlat)+ "&lomin=" + str(minlong) + "&lamax=" + str(maxlat) + "&lomax=" + str(maxlong))
      #  print(restreq)
        holddata = restreq.text
        holddata = holddata[int(holddata.find("states")) + 8:]
        holddata = holddata.split("],")
        holdout = []
        for idx,i in enumerate(holddata):
            holddata[idx] = i.split(',')
            if idx == 0:
                holddata[idx][0] = holddata[idx][0][holddata[idx][0].find("[[") + 2:]
            if idx == (len(holddata) - 1):
                holddata[idx][16] = holddata[idx][16][0]
    return (holddata)
