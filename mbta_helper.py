# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPQUEST_API_KEY, MBTA_API_KEY
import urllib.request
from urllib.request import urlopen
from urllib import response
import json
from pprint import pprint
import requests

#mbta api key

url = f'http://mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College,MA'


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

#API Keys
MAPQUEST_API_KEY = 'S5SVapgODzwYR0PwEBr38vbVGVXUt3iP'
MBTA_API_KEY = '9d03cd45f08e4c6f9df565bd68d14cc7'

# A little bit of scaffolding if you want to use it


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)

    return (response_data)


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    place_name = place_name.replace(' ', '%20')
    response_data = get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name},MA')
    latitude_longitude = response_data['results'][0]['locations'][0]['latLng']
    latitude_longitude = tuple(latitude_longitude.values())
    lat = latitude_longitude[0]
    long = latitude_longitude[1]
    return lat, long

#get_lat_long('Washington,D.C')

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
 
    strlat = str(latitude)
    strlong = str(longitude)


    jsonfile = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={strlat}&filter%5Blongitude%5D={strlong}'
 

    mbta_response_data = get_json(jsonfile)
    name_of_station = mbta_response_data.get("data"[0])
 

    print(name_of_station)
  

    # mbta_response_data = get_json(url)
    # wheelchair_accessible = mbta_response_data['data'][0]['attributes']['wheelchair_boarding']
    # name_of_station = mbta_response_data['data'][0]['attributes']['name']
    # if wheelchair_accessible == 1:
    #     wheelchair_accessible = 'Wheelchair Accessible'
    # elif wheelchair_accessible == 2:
    #     wheelchair_accessible = 'Wheelchair Inaccessible'
    # else:
    #     wheelchair_accessible = 'No data found'
    # print(name_of_station, wheelchair_accessible)

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    res = get_lat_long(place_name)
    print(res)
    return get_nearest_station(res[0], res[1])
    

def main():
    """
    You can test all the functions here
    """
    #get_json(url)
    #get_lat_long('Boston Commons, Boston')
    #get_nearest_station(42.3601, 71.0589)
    find_stop_near('Fenway, Boston')


if __name__ == '__main__':
    main()
