import json, requests, math, pygal



# opensky stuff goes here

def planeswithin(minlat, maxlat, minlong, maxlong, test = False):
    if not(test):
        restreq = requests.get("https://opensky-network.org/api/states/all?lamin=" +  str(minlat)+ "&lomin=" + str(minlong) + "&lamax=" + str(maxlat) + "&lomax=" + str(maxlong))
        # print(restreq)
        holddata = restreq.text
        holddata = holddata[int(holddata.find("states")) + 8:]
        holddata = holddata.split("],")
        # print(holddata)
        try:
            for idx,i in enumerate(holddata):
                holddata[idx] = i.split(',')
                if idx == 0:
                    holddata[idx][0] = holddata[idx][0][holddata[idx][0].find("[[") + 2:]
                if idx == (len(holddata) - 1):
                    print("holddata idx: {}".format(holddata[idx]))
             #       print("holddata arr: {}".format(holddata[idx][16][0]))
                    holddata[idx][16] = holddata[idx][16][0]
        except:
            print('hell')
    # print(holddata[0])
  #  if(len(holddata) == 0):

    return (holddata)


