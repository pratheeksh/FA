#!/usr/bin/python
#We will use the haversive formula to calculate distance between two gps points
from math import radians, cos, sin, asin, sqrt, atan2

def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a),sqrt(1-a))
    r = 6371 # Radius of earth in kilometers.
    return c * r
def calcDetour(latArray,longArray):
    AC=haversine(longArray[0],latArray[0],longArray[2],latArray[2])
    CD=haversine(longArray[2],latArray[2],longArray[3],latArray[3])
    DB=haversine(longArray[3],latArray[3],longArray[1],latArray[1])
    CA=haversine(longArray[2],latArray[2],longArray[0],latArray[0])
    AB=haversine(longArray[0],latArray[0],longArray[1],latArray[1])
    BD=haversine(longArray[1],latArray[1],longArray[3],latArray[3])
    driver1_DD=AC+CD+DB #Detour distance for driver 1
    driver2_DD=CA+AB+BD #Detour distance for driver 2
    return min(driver1_DD,driver2_DD)

latArray = []
longArray = []
for c in "ABCD":
    print "Enter the latitude and longitude of location", c
    x = int(input("Latitude: "))
    y = int(input("Longitude: "))
    latArray.append(x)
    longArray.append(y)
print "Minimum Detour Distance", calcDetour(latArray,longArray)
