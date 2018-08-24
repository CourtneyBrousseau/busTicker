#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home
sleep 5s
cd /
cd home/pi/realtime-subscriber-counter
sudo python ticker.py
cd /
