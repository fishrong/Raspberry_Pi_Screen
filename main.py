# -*- coding:UTF-8 -*-
import threading
import traceback

import RPi.GPIO as GPIO
import OLED_Driver as OLED
from Oled_Screen_1_5 import show_theme_spaceman

try:
    def main():
        OLED.Device_Init()
        show_theme_spaceman()
    if __name__ == '__main__':
        main()

except Exception as e:
    print("\r\nEnd")
    traceback.print_exc()
    OLED.Clear_Screen()
    GPIO.cleanup()
