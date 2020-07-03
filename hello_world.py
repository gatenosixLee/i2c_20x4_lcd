import lcddriver as lcd
from time import time
from time import sleep
from datetime import datetime
import sys

bus = 2

argv = sys.argv
if len(argv) > 1:
    bus = int(argv[1])
lcd = lcd.lcd(bus)

lcd.display_string("20x4 LCD Example", 1)
lcd.display_string("Hello ODROID", 2)

while True:
  dateString = datetime.now().strftime('%b %d %y')
  timeString = datetime.now().strftime('%H:%M:%S')
#   lcd.display_string(dateString, 3)
#   lcd.display_string(timeString, 4)
  sleep(1)
