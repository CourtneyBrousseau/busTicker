#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home
sleep 10s
cd /
cd home/pi/bus-tracker
sudo python ticker.py
cd /
