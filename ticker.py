
# ticker.py
import json
import sys
import argparse
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

busStops = ["52223", "52244", "53677", "50144"]
busRoutes = ["51B", "79"]
busList = []
NEXT_BUS_API_BASE = "http://webservices.nextbus.com/service/publicXMLFeed?"

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
                                bus = routeName + " " + toward + " in " + minutes + " min"
				busList.append(bus)
				print(bus)

def displayBus():
	if (len(busList) == 0):
		device.show_message("No buses :(", font=proportional(TINY_FONT))
	else:
		bus = busList.pop(0)
		device.show_message(bus, font=proportional(TINY_FONT))

if __name__ == '__main__':
	device = led.matrix(cascaded = 8)
	device.orientation(90)

	#schedule.every(1).seconds.do(showBuses)

	# Run the scheduler
       	while True:
                showBuses()
                time.sleep(1)
