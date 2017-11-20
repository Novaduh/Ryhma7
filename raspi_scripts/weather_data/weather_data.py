#! python3 - weather_data

import requests
import openpyxl
import json
import sys
import datetime
import time
import xml.etree.ElementTree as ET

# TODO: proper placement for this function
def get_time():  # Get time and format it for the link
    timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:00:00Z')
    return str(timestamp)


# Constants
API_KEY = 'a42452aa-ef80-4041-9668-4aa5007f61ef'
PLACE = 'lahti'
START_TIME = get_time()
END_TIME = get_time()
TIMESTEP = 60  # min
SLEEPTIME = 5  # s
LINK = ('http://data.fmi.fi/fmi-apikey/%s/wfs?request=getFeature'
    '&storedquery_id=fmi::forecast::hirlam::surface::point::timevaluepair'
    '&place=%s&parameters=Temperature,WeatherSymbol3&starttime=%s&endtime=%s'
    '&timestep=%s') % (API_KEY, PLACE, START_TIME, END_TIME, str(TIMESTEP))

def get_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return (response.text)

def xml_parse(data):
    root = ET.fromstring(data)
    return root

def get_weather_data(XML_DATA):
    indexPosition = 0
    weatherData = {'temperature': 0, 'weather_icon': 0}
    for value in XML_DATA.iter('{http://www.opengis.net/waterml/2.0}value'):
        if indexPosition == 0:
            weatherData['temperature'] = float(value.text)
        elif indexPosition == 1:
            weatherData['weather_icon'] = float(value.text)
        indexPosition += 1
    return weatherData

def is_location_given():
    # TODO
    return



def main():
    while True:
        #print(LINK)
        data = xml_parse(get_data(LINK))
        print(get_weather_data(data))
        with open('data.json', 'w') as fp:
            json.dump(get_weather_data(data), fp)
        time.sleep(SLEEPTIME)

if __name__ == "__main__":
    main()
