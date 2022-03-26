# -*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import OLED_Driver as OLED
from Oled_Screen_1_5 import show_screen_1

try:
    def main():
        OLED.Device_Init()
        print("init end")
        while True:
            show_screen_1()
            OLED.Delay(100)
    if __name__ == '__main__':
        main()

except Exception as e:
    print("\r\nEnd")
    print(e)
    OLED.Clear_Screen()
    GPIO.cleanup()
