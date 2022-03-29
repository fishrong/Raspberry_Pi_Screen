# 一、说明
此项目是使用树莓派的IO接口驱动OLED屏幕，效果如下：
![https://github.com/fishrong/Raspberry_Pi_Screen/blob/master/IMG_3618.JPG](https://github.com/fishrong/Raspberry_Pi_Screen/blob/master/IMG_3618.JPG)

# 二、环境依赖
**软件依赖**
* opencv
* PIL
* GPIO

**硬件**
* 树莓派
* 1.54 OLED屏幕

1. 上述中opencv不太好折腾，需要在树莓派中编译安装，
官网[文档](https://docs.opencv.org/4.x/d2/de6/tutorial_py_setup_in_ubuntu.html) 
，网友[教程](https://zhuanlan.zhihu.com/p/46032511)
2. OLED连接及示例[教程](https://wiki.diustou.com/cn/1.5inch_RGB_OLED_Module)

# 三、思路
1. 使用PIL的画图方法显示文字信息，动画则是使用opencv获取视频帧，绘制在屏幕上。
`静止是绝对的，运动是相对的。视频的显示实质是显示的一张一张图片,有点像小时候的胶片电影`
2. 屏幕显示优化，如果显示数据较多，获取数据较耗时，会影响屏幕的显得有点卡顿。优化思路是，
减少耗时操作或耗时操作异步化，另一个时，错峰加载，不同时间节点加载不同的数据。


# 四、使用
```commandline
sudo python3 main.py
```
