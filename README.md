# 一、说明
此项目是使用树莓派的IO接口驱动OLED屏幕，效果如下：
![https://github.com/fishrong/Raspberry_Pi_Screen.git/master/IMG_3618.jpg](IMG_3618.jpg)

# 二、环境依赖
* opencv
* PIL
* GPIO

上述中opencv不太好折腾，需要在树莓派中编译安装，
官网[文档](https://docs.opencv.org/4.x/d2/de6/tutorial_py_setup_in_ubuntu.html) 
，网友[教程](https://zhuanlan.zhihu.com/p/46032511)

# 三、思路
使用PIL的画图方法显示文字信息，动画则是使用opencv获取视频帧，绘制在屏幕上。
`静止是绝对的，运动是相对的。视频的显示实质是显示的一张一张图片`


# 四、使用
```commandline
sudo python3 main.py
```
