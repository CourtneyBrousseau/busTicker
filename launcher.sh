#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/realtime-subscriber-counter
sudo python ticker.py
cd /
