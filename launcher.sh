#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/bus-tracker
sudo python loading.py
sudo python ticker.py
cd /
