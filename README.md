# Bus Tracker
An LED Matrix that displays AC transit bus predictions in realtime.

Based on a tutorial [here](https://youtu.be/HN2RRBSAsn8). See more instructions about how to make the device on [hackster.io](https://www.hackster.io/hackerhouse/realtime-cryptocurrency-ticker-youtube-subscriber-counter-0ac8c5).

## Pre-requisites
+ Python 2.7
+ pip
+ Raspbian

## Wiring

| Board Pin	| Name	| Remarks	|RPi Pin |	RPi Function
|-----|------|------| -----|-----|
|1	|VCC	|+5V Power	|2	|5V0
|2	|GND	|Ground	|6	|GND
|3	|DIN	|Data In	|19	|GPIO 10 (MOSI)
|4	|CS	|Chip Select	|24	|GPIO 8 (SPI CE0)
|5	|CLK	|Clock	|23	|GPIO 11 (SPI CLK)

## Install Dependencies 

Before you run the program, make sure to install dependencies. Navigate to the project directory and run

```
pip install -r requirements.txt
```

to install the python dependencies. 

Enable the SPI driver for the max7219 LED module to work properly.

```
sudo raspi-config
```

Scroll down to `Advanced Options` (`Interfacing Options` on the Pi Zero) and press enter.

Scroll down to `SPI`, press enter, and select `yes`.

Reboot.

## Running the Program

Run `python ticker.py`
