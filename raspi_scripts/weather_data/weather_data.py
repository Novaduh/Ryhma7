#! python3 - weather_data

import requests
import json
import datetime
import time
import xml.etree.ElementTree as ET

def get_time():  # Get time and format it for the link
    timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:00:00Z')
    return str(timestamp)


# Constants
API_KEY = 'a42452aa-ef80-4041-9668-4aa5007f61ef'
PLACE = 'lahti'
START_TIME = get_time()  # Weather data from (time)
END_TIME = get_time()  # Weather data to (time)
TIMESTEP = 60  # min
SLEEPTIME = 900  # s
LINK = ('http://data.fmi.fi/fmi-apikey/%s/wfs?request=getFeature'
    '&storedquery_id=fmi::forecast::hirlam::surface::point::timevaluepair'
    '&place=%s&parameters=Temperature,WeatherSymbol3&starttime=%s&endtime=%s'
    '&timestep=%s') % (API_KEY, PLACE, START_TIME, END_TIME, str(TIMESTEP))

def get_data(url):  # Request data from api server
    response = requests.get(url)
    response.raise_for_status()
    return (response.text)

def xml_parse(data):  # Parse text data into xml format
    root = ET.fromstring(data)
    return root

def get_weather_data(XML_DATA):  # Get weather and temperature parameters
    indexPosition = 0
    weatherData = {'temperature': 0, 'weather_icon': 0}
    for value in XML_DATA.iter('{http://www.opengis.net/waterml/2.0}value'):
        if indexPosition == 0:
            weatherData['temperature'] = float(value.text)  # Temperature
        elif indexPosition == 1:
            weatherData['weather_icon'] = float(value.text)  # Weather
        indexPosition += 1
    return weatherData

def main():  # Main loop
    while True:
        data = xml_parse(get_data(LINK))
        with open('data.json', 'w') as fp:  # Store data into JSON file
            json.dump(get_weather_data(data), fp)
        time.sleep(SLEEPTIME)  # Wait for next cycle

if __name__ == "__main__":
    main()
