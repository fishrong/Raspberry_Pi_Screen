import cv2
from PIL import ImageFont, Image

font_cn_12 = ImageFont.truetype('./res/851DianJiWenZiTi-2.ttf', 12)
font_cn_16 = ImageFont.truetype('./res/851DianJiWenZiTi-2.ttf', 16)
font_cn_28 = ImageFont.truetype('./res/851DianJiWenZiTi-2.ttf', 28)


def vido_init():
    img_list = []
    video_capture = cv2.VideoCapture("res/spaceman-small.mp4")
    index = 0
    while True:
        success, frame = video_capture.read()
        if success:
            index = index + 1
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            re_image = image.resize((50, 50), Image.ANTIALIAS)
            if index % 4 == 0:
                buffer = re_image.load()
                img_list.append(buffer)
        else:
            break
    return img_list
