import max7219.led as led
from max7219.font import proportional, TINY_FONT
from custom_font import CUSTOM_FONT
import time

if __name__ == '__main__':
        device = led.matrix(cascaded = 8)
        device.orientation(90)

	device.show_message("Loading ...", font=proportional(TINY_FONT))
        time.sleep(10)
