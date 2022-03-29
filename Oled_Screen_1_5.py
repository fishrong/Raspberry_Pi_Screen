import threading
import time

from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO
import OLED_Driver as OLED
from Draw_Util import font_cn_16, font_cn_28, font_cn_12, vido_init
from System_Info import get_ram_info, get_disk_space, get_cpu_temperature, get_cpu_use, get_ram_percent, \
    get_disk_space_percent

img_count = 0
img_list = vido_init()
week_arr = ['日', '一', '二', '三', '四', '五', '六']
ram_per = '0'
disk_perc = '0'
cpu_temp = '0'
cpu_usage = '0'


def show_video():
    # print("show video begin")
    global img_count
    img_count = img_count + 1
    if img_count > len(img_list) - 1:
        img_count = 0
    # 太空人
    OLED.display_image_from_cache(img_list[img_count], 70, 41, 50, 50)


def show_theme_spaceman():
    # print("show image begin")
    while True:
        # 背景
        # start = time.time()
        if time.localtime().tm_sec == 59:
            # 时间
            cur_time = time.localtime()
            cur_time_hm = time.strftime("%H:%M", cur_time)
            cur_time_w = '周' + week_arr[int(time.strftime("%w", cur_time))]
            cur_time_d = time.strftime("%d", cur_time)
            img_top = Image.new("RGB", (OLED.SSD1351_WIDTH, 40), "black")
            draw = ImageDraw.Draw(img_top)
            draw.text((0, 0), cur_time_w, fill="RED", font=font_cn_16)
            draw.text((0, 20), cur_time_d, fill="BLUE", font=font_cn_16)
            draw.text((34, 0), cur_time_hm, fill="WHITE", font=font_cn_28)
            OLED.display_image_from_cache(img_top.load(), 0, 0, OLED.SSD1351_WIDTH, 40)
        if time.localtime().tm_sec % 7 == 0:
            img_mid_left = Image.new("RGB", (65, 50), "black")
            draw_mid_left = ImageDraw.Draw(img_mid_left)
            # 分割线
            draw_mid_left.rectangle((0, 0, 65, 2), fill="white")
            draw_mid_left.text((0, 10), 'RAM: ' + str(int(ram_per * 100)) + '%', fill="WHITE", font=font_cn_12)
            # 磁盘容量使用百分比
            draw_mid_left.text((0, 30), 'DISK: ' + disk_perc, fill="WHITE", font=font_cn_12)
            OLED.display_image_from_cache(img_mid_left.load(), 0, 41, 65, 50)

        if time.localtime().tm_sec % 3 == 0:
            threading.Thread(target=get_system_info).start()
            img_bottom = Image.new("RGB", (OLED.SSD1351_WIDTH, 38), "black")
            draw_bottom = ImageDraw.Draw(img_bottom)
            draw_bottom.text((0, 2), 'CPU Temp: ' + cpu_temp + '℃', fill="WHITE", font=font_cn_12)
            # CPU使用百分比
            draw_bottom.text((0, 20), 'CPU Usage: ' + cpu_usage + '%', fill="WHITE", font=font_cn_12)
            OLED.display_image_from_cache(img_bottom.load(), 0, 91, OLED.SSD1351_WIDTH, 37)
        show_video()
        # print("show time"+str(time.time()-start))
        OLED.Delay(100)


def get_system_info():
    global ram_per, disk_perc, cpu_temp, cpu_usage
    ram_per = get_ram_percent()
    disk_perc = get_disk_space_percent()
    cpu_temp = get_cpu_temperature()
    cpu_usage = get_cpu_use()
