
# ticker.py
import requests
import json
import sys
import argparse
import schedule
import time
import functools
import max7219.led as led
from max7219.font import proportional, TINY_FONT
from custom_font import CUSTOM_FONT
from datetime import datetime
import urllib2
import xml.etree.ElementTree

#this makes it work
import spidev
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 15600000

#set the date and time format
date_format = "%m-%d-%Y %H:%M:%S"
bus_date_format ="%Y-%m-%dT%H:%M:%S" 
# add command line arguments
parser = argparse.ArgumentParser(description='Realtime statistics counter')

parser.add_argument('--busStop', dest='busStop',
		   help='your bus stop')
parser.add_argument('--apiKey', dest='apiKey',
                   help='your NextBus API key')

args = parser.parse_args()

busStops = ["52223", "52244", "53677", "50144"]
busRoutes = ["51B", "79"]
busList = []
NEXT_BUS_API_BASE = "http://webservices.nextbus.com/service/publicXMLFeed?"

def getBuses(b, ak):
        """
        Fetches crypto currency prices. 
        If the specified currency does not exist, return None. Otherwise, return the price in USD. 

        API docs: https://coinmarketcap.com/api/
        """
	now = datetime.now()
	nowstr = now.strftime(date_format)
	nowTime = datetime.strptime(nowstr, date_format)

        try:
		url = "http://api.actransit.org/transit/stops/"
		url += b
		url += "/predictions/?token="
		url += ak 
                r = requests.get(url)
                data = json.loads(r.text)
		routes = ""
                for bus in data:
                        routes += bus['RouteName'] + " - "
			busTime = datetime.strptime(bus['PredictedDeparture'], bus_date_format)
			diff = busTime - nowTime
        		minutes = (diff.seconds) / 60 - 1020
			routes += str(minutes) + " min   "

		return routes

                print "Cryptocurrency not found in response data"
                return None

        except Exception as e:
                print str(e)
                return None

def updateCounter(job_func, *args, **kwargs):
	"""
	Updates the LED matrix with the current count. Values are fetched from the specified job func,
	"""

	ret = functools.partial(job_func, *args, **kwargs)()
	device.show_message(ret, font=proportional(TINY_FONT))

def showBuses():
	if (len(busList) == 0):
		updateBusList()
	displayBus()

def updateBusList():
        for stop in busStops:
		getUpcomingDeparturesFromStop(stop)

def getUpcomingDeparturesFromStop(stop):
	response = urllib2.urlopen(NEXT_BUS_API_BASE + "command=predictions&a=actransit&stopId=" + stop)
        bus_departures = xml.etree.ElementTree.parse(response).getroot()
        for route in bus_departures.findall('predictions'):
        	routeName = route.get("routeTag")
		if routeName in busRoutes and not route.get("dirTitleBecauseNoPredictions"):
                	for direction in route.findall("direction"):
                        	toward = direction.get("title")
                                minutes = direction[0].get("minutes")
                                busList.append(routeName + " -> " + toward + " : " + minutes + " min.")
				speech_output = routeName + " bus toward " + toward + " in " + minutes + " minutes. "
				print(speech_output)

def displayBus():
	if (len(busList) == 0):
		device.show_message("No buses :(", font=proportional(TINY_FONT))
	else:
		bus = busList.pop(0)
		device.show_message(bus, font=proportional(TINY_FONT))

if __name__ == '__main__':
	device = led.matrix(cascaded = 8)
	device.orientation(90)

	schedule.every(1).seconds.do(showBuses)

	# Run the scheduler
       	while True:
                schedule.run_pending()
                time.sleep(1)
	if (args.busStop is not None):
		#time.sleep(2)

                schedule.every(5).seconds.do(updateCounter, getBuses, args.busStop, args.apiKey)

                # Run the scheduler
                while True:
                        schedule.run_pending()
                        time.sleep(1)





