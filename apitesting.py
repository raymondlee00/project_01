import json, requests, math, pygal
from opensky_api import OpenSkyApi
from scrapers import location


# opensky stuff goes here
#todo: convert to rest api
def planeswithin(minlat, maxlat, minlong, maxlong, test = False):
    api = OpenSkyApi()
    if not(test):
        restreq = "https://opensky-network.org/api/states/all?lamin=" +  str(minlat)+ "&lomin=" + str(minlong) + "&lamax=" + str(maxlat) + "&lomax=" + str(maxlong)
        print(restreq)
        try:
            states = api.get_states(bbox=(minlat, maxlat, minlong, maxlong))
            holdout = []
            for s in states.states:
                holdout.append("(%r, %r, %r, %r, %r, %r, %r)" % (
                s.latitude, s.longitude, s.baro_altitude, s.velocity, s.heading, s.icao24, s.callsign))
        except:
            holdout = ["(40.6971, -73.3389, 5036.82, 170.96, 15, 'a1c5fd', 'JIA5282 ')", "(40.9308, -74.2128, 4366.26, 158.84, 259.93, 'aa8c1b', 'SWA2376 ')", "(40.9124, -73.3609, 7863.84, 236.47, 48.26, 'a3a575', 'JBU626  ')", "(39.9116, -74.6691, 4305.3, 173.41, 85.41, 'a7ceb2', 'PDT4926 ')", "(41.0459, -74.2104, 746.76, 77.79, 142.52, 'acdfe5', 'N929DA  ')", "(41.1322, -73.9961, 1569.72, 81, 64.41, 'ada641', 'N979NA  ')", "(40.5992, -73.7909, 167.64, 67.32, 30.29, 'a0f4b5', 'DAL47   ')", "(40.7779, -73.8766, 38.1, 15.43, 50, 'a53436', 'RPA4535 ')", "(40.7006, -74.2939, 640.08, 99.84, 68.86, 'a7d740', 'N604MT  ')", "(40.6904, -74.198, 312.42, 9.16, 128.16, 'a4fa89', 'N42NY   ')", "(41.1266, -74.3684, 6202.68, 203.37, 272.32, 'aba281', 'AAL2369 ')", "(41.137, -74.5085, 2133.6, 140.56, 197.9, 'aa44cd', 'UAL71   ')", "(40.578, -74.1178, 1432.56, 128.64, 76.35, 'a21bea', 'RPA6120 ')", "(40.3732, -73.8455, 952.5, 102.89, 292.33, 'a63b04', 'N500MA  ')", "(40.7273, -73.7249, 12496.8, 270.77, 48.47, 'a88e98', 'N650VC  ')", "(40.8888, -74.0477, 624.84, 115.3, 332.06, 'a69bfe', 'N525F   ')", "(40.777, -73.8732, None, 0, 154, 'ac7e09', 'AAL1330 ')", "(41.566, -74.726, 8763, 236.41, 299.74, 'aa8be5', 'EJA779  ')", "(40.6394, -74.6495, 8534.4, 204.55, 231.23, 'a4d621', 'SWA2416 ')", "(40.5622, -74.2676, 4892.04, 180.09, 198.49, 'a4c328', 'XOJ406  ')", "(40.7762, -73.8731, None, 0, 109, 'ad5436', 'AAL2848 ')", "(40.841, -74.5465, 1600.2, 136.86, 179.14, 'a0a522', 'UAL56   ')", "(41.1294, -73.4797, 5173.98, 211.72, 45.59, '896117', 'UAE224  ')", "(40.6913, -74.1655, 30.48, 53.84, 26.08, 'a95c89', 'FFT122  ')", "(40.6599, -74.54, 5158.74, 187.9, 234.13, 'a1c57e', 'RPA5934 ')", "(40.7738, -73.8646, None, 10.8, 120, 'a437b5', 'EDV5287 ')", "(41.2485, -74.342, 4739.64, 210.32, 326.78, 'a4000f', 'DAL1496 ')", "(39.9123, -73.3231, 10363.2, 209.95, 223.71, 'a3b808', 'JBU1081 ')", "(40.2209, -74.2934, 6324.6, 189.83, 37.18, 'a8a6c0', 'PDT4974 ')", "(40.0546, -73.0623, 13106.4, 197.53, 225.32, 'a403f4', 'EJA358  ')", "(41.482, -73.8139, 10972.8, 202.84, 177.82, 'a2882a', 'N262TX  ')", "(40.6926, -74.1719, None, 5.92, 120, 'a8102a', 'UAL1527 ')", "(41.3844, -73.1093, 5791.2, 186.49, 80.95, 'a332f5', 'GLT305  ')", "(40.6989, -74.1645, 213.36, 75.36, 29.89, 'a1073f', 'ASQ4269 ')", "(40.6978, -74.5229, 937.26, 79.38, 117.4, 'aa8eac', 'N78FB   ')", "(41.0078, -73.6609, 533.4, 61.68, 328.3, 'aa2e0b', 'EJA755  ')", "(40.5822, -73.8041, 365.76, 65.29, 30.81, '40073d', 'BAW117  ')", "(40.7886, -74.3372, 2255.52, 142.46, 258.12, 'a28947', 'UAL663  ')", "(40.7626, -73.9296, 1249.68, 137.13, 256.33, 'a871cf', 'EJA643  ')", "(40.0911, -73.7398, 6217.92, 230.85, 110.62, 'a8d4f6', 'UAL1470 ')", "(39.8572, -74.3942, 7353.3, 208.37, 216.16, 'ac767c', 'AAL2024 ')", "(40.4852, -73.8795, 640.08, 85.14, 30.9, 'a87f50', 'AVA210  ')", "(40.666, -73.726, 746.76, 93.11, 90, 'a009a4', 'AAL179  ')", "(40.6014, -73.4118, 655.32, 73.06, 359.19, 'a700a3', 'EDG550  ')", "(40.8582, -74.2487, 1524, 139.05, 239.55, 'a0339a', 'UCA4994 ')", "(40.8121, -73.3199, 10668, 269.25, 43.76, '8964b2', 'UAE232  ')", "(40.5129, -74.2853, 937.26, 101.76, 57.6, 'a0822c', 'UCA4884 ')", "(40.4699, -73.1119, 8481.06, 209.59, 206.38, 'a38d48', 'AAY2271 ')", "(40.799, -74.1279, 1424.94, 137.8, 287.83, 'a0a9b2', 'UCA4918 ')", "(39.8832, -74.7458, 647.7, 121.51, 37.26, 'ae0449', '')", "(40.688, -73.1734, 2286, 150.55, 235.44, 'aa3417', 'AAL45   ')", "(40.4914, -73.6889, 1562.1, 140.56, 198.57, '424476', 'AFL100  ')", "(40.7256, -73.5458, 1935.48, 154.99, 46.08, '869210', 'ANA9    ')", "(40.6108, -74.4732, 1546.86, 130.44, 122.44, 'a3cf6d', 'UAL1812 ')", "(40.915, -73.6443, 1249.68, 137.82, 207.33, 'c00fab', 'SKV7632 ')", "(39.8547, -73.9758, 3924.3, 190.79, 29.74, 'a683a8', 'JBU502  ')", "(41.2775, -73.5857, 9144, 217.58, 230.85, 'a4d011', 'SWA2125 ')", "(40.1732, -74.5367, 3086.1, 184.65, 47.82, 'a97020', 'SWA928  ')", "(40.7939, -74.5468, 937.26, 90.75, 201.62, 'a813e9', 'N62AE   ')", "(40.778, -73.8768, 38.1, 33.44, 30.51, 'ac78b0', 'EDV5069 ')", "(40.7559, -74.204, 487.68, 87.8, 48.09, '424153', 'VPCPX   ')", "(39.9596, -74.8438, 3855.72, 180.64, 47.77, 'a42b45', 'DAL2748 ')", "(40.8524, -74.0491, 7620, 224.94, 4.33, 'a92e72', 'PDT4792 ')", "(40.796, -73.5402, 8229.6, 240.82, 50.46, 'aa0e62', 'AAL2129 ')", "(39.8969, -74.9207, 9448.8, 261.66, 46.67, 'a707a3', 'JBU1806 ')", "(41.0863, -74.0594, 5204.46, 209.12, 276.36, 'ad60b7', 'JBU615  ')", "(41.4656, -73.5565, 10607.04, 245.15, 5.9, 'a769a3', 'JIA5628 ')", "(40.3299, -73.5106, 9456.42, 251.84, 56.67, 'ac9aae', 'DAL406  ')", "(40.9892, -74.3915, 3421.38, 170.44, 346.38, 'aa0b10', 'RPA3497 ')", "(40.0279, -73.573, 10142.22, 172.3, 221.97, 'a7ff09', 'EJA614  ')", "(41.1382, -73.8727, 1249.68, 140.4, 303.34, 'a8c484', 'EJA664  ')", "(40.717, -74.215, 3352.8, 137.66, 195.39, 'a37e9b', 'EJA324P ')", "(41.505, -73.8196, 9144, 190.62, 230.04, 'aa3908', 'EJM6    ')", "(40.7753, -73.8747, None, 0, 61, 'a0d72b', 'AAL1788 ')", "(41.4291, -74.1406, 2194.56, 142.06, 238.32, 'a37df6', 'JBU2479 ')", "(40.7214, -73.9234, 419.1, 60.53, 31.8, 'a1c1c7', 'RPA6057 ')", "(40.8643, -74.572, 11582.4, 220.13, 229.83, 'ab120b', 'DAL83   ')", "(40.6551, -74.1885, 220.98, 60.51, 25.69, 'a1d63d', 'UAL1766 ')", "(40.6685, -74.18, 76.2, 61.2, 25.92, 'a36fbf', 'EJA320P ')", "(39.9984, -74.5413, 7338.06, 219.03, 46.14, 'a230d1', 'N240JK  ')", "(40.9293, -73.5507, 4244.34, 186.01, 317.13, 'ac575b', 'EDV3364 ')", "(40.4522, -74.4515, 2545.08, 143.51, 70.53, 'acdaec', 'EJM273  ')", "(40.8525, -74.0648, 30.48, 0, 137, '4d21d8', 'VCJ91S  ')", "(40.7092, -74.3596, 937.26, 59.52, 67.65, 'a0c8bb', 'HPK15   ')", "(40.5968, -73.7927, 167.64, 68.47, 30.23, 'a3c880', 'AAL54   ')", "(40.7195, -74.9099, 4892.04, 187.12, 254.21, 'a65156', 'ASH6260 ')", "(40.4333, -73.9192, 632.46, 72.94, 27.29, 'a471e0', 'DAL2843 ')", "(41.2133, -74.1714, 10980.42, 212.03, 221.85, 'a1e9af', 'AAY1530 ')", "(40.8559, -74.0618, 30.48, 2.31, 309, '4d2155', 'VJT993  ')", "(41.1316, -74.1022, 6096, 202.99, 186.55, 'ac41c0', 'EDV3470 ')", "(40.4792, -73.4703, 1211.58, 141.96, 248.08, '7100c8', 'SVA021  ')", "(41.2131, -74.6283, 1424.94, 134.29, 168.73, 'a67fba', 'LXJ518  ')", "(40.8344, -73.9099, 1143, 111.31, 15, 'ab6b04', 'EDV3349 ')", "(41.6613, -73.2991, 10050.78, 218.9, 238.55, 'a6ab27', 'JBU1139 ')"]
    if test:
        holdout = ["(40.6971, -73.3389, 5036.82, 170.96, 15, 'a1c5fd', 'JIA5282 ')", "(40.9308, -74.2128, 4366.26, 158.84, 259.93, 'aa8c1b', 'SWA2376 ')", "(40.9124, -73.3609, 7863.84, 236.47, 48.26, 'a3a575', 'JBU626  ')" ]
    for idx, i in enumerate(holdout):

        holdmeh = i.split(',')
        try:
            holdmeh[0] = float(holdmeh[0][1:])
            holdmeh[1] = float(holdmeh[1])
            holdmeh[2] = float(holdmeh[2])
            holdmeh[3] = float(holdmeh[3])
            holdmeh[4] = float(holdmeh[4])
            holdout[idx] = holdmeh
        except ValueError:
            del holdout[idx]
    return (holdout)

planeswithin(39.7263, 41.7263, -74.9818, -72.9818)


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
#print(planes_near_me(1, 1))

# 40.7263 + -0.2559971502571034
# -73.9818 + 1.4164236861550314
#
#         40.4703028497429,-72.56537631384498
