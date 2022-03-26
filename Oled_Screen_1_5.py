import time

from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO
import OLED_Driver as OLED
from Draw_Util import font_cn_16, font_cn_32, font_cn_12, vido_init
from System_Info import get_ram_info, get_disk_space, get_cpu_temperature, get_cpu_use, get_ram_percent, \
    get_disk_space_percent

img_count = 0
img_list = vido_init()
week_arr = ['日', '一', '二', '三', '四', '五', '六']
# 场景1
def show_screen_1():
    global img_count
    img_count = img_count + 1
    if img_count > len(img_list) - 1:
        img_count = 0
    # 背景
    img_background = Image.new("RGB", (OLED.SSD1351_WIDTH, OLED.SSD1351_HEIGHT), "black")
    draw = ImageDraw.Draw(img_background)
    # 时间
    cur_time = time.localtime()
    cur_time_hm = time.strftime("%H:%M", cur_time)
    cur_time_w = '周' + week_arr[int(time.strftime("%w", cur_time))]
    cur_time_d = time.strftime("%d", cur_time)
    draw.text((0, 6), cur_time_w, fill="RED", font=font_cn_16)
    draw.text((0, 23), cur_time_d, fill="BLUE", font=font_cn_16)
    draw.text((40, 5), cur_time_hm, fill="WHITE", font=font_cn_32)

    # 分割线
    draw.rectangle((0, 50, 60, 52), fill="white")

    # 系统信息
    # ram使用百分比
    ram_per = get_ram_percent()
    draw.text((0, 60), 'RAM: ' + str(int(ram_per * 100)) + '%', fill="WHITE", font=font_cn_12)
    # 磁盘容量使用百分比
    disk_perc = get_disk_space_percent()
    draw.text((0, 75), 'DISK: ' + disk_perc, fill="WHITE", font=font_cn_12)
    # CPU温度
    cpu_temp = get_cpu_temperature()
    draw.text((0, 90), 'CPU Temp: ' + cpu_temp + '℃', fill="WHITE", font=font_cn_12)
    # CPU使用百分比
    cpu_usage = get_cpu_use()
    draw.text((0, 105), 'CPU Usage: ' + cpu_usage + '%', fill="WHITE", font=font_cn_12)
    # 太空人动画
    img_background.paste(img_list[img_count], (70, 37))
    OLED.Display_Image(img_background)
