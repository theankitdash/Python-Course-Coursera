from urllib.parse import urlencode
from urllib.request import urlopen
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input("Enter location: ")
    if len(address) < 1 : break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key

    url = serviceurl + urlencode(parms)
    print ('Retrieving', url)

    uh = urlopen(url)
    data = uh.read()
    print ('Retrieved',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print ('Failure To Retrieve')
        print (data)
        continue


    placeid = js["results"][0]['place_id']
    print ("Place id", placeid)

