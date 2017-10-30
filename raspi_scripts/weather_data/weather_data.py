#! python3 - weather_data

import requests
import openpyxl
import json
import sys
import datetime
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring

# Constants
API_KEY = 'a42452aa-ef80-4041-9668-4aa5007f61ef'
PLACE = 'lahti'
START_TIME = '2017-10-30T14:00:00Z' # TODO: get_time() format
END_TIME = '2017-10-30T17:00:00Z'   # TODO: get_time() format
TIMESTEP = 60  # min
LINK = ('http://data.fmi.fi/fmi-apikey/%s/wfs?request=getFeature'
    '&storedquery_id=fmi::forecast::hirlam::surface::point::timevaluepair'
    '&place=%s&parameters=Temperature,WeatherSymbol3&starttime=%s&endtime=%s'
    '&timestep=%s') % (API_KEY, PLACE, START_TIME, END_TIME, str(TIMESTEP))

def get_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def convert_to_json(data):
    return json.dumps(bf.data(fromstring(data)))

def get_time():  # DO NEXT
    timestamp = datetime.datetime.now()
    timestamp.strftime('%Y-%m-%dT%H:00:00Z')
    print(timestamp)
    return str(timestamp)

def get_wanted_data():
    # TODO
    return

def is_location_given():
    # TODO
    return

def main():
    get_time()
    print(LINK)
    json = convert_to_json(get_data(LINK))
    print(json)


if __name__ == "__main__":
    main()