# 轮廓：入门
# 学习查找和绘制轮廓
#
# 目标
# 了解轮廓是什么。
# 学习寻找轮廓，绘制轮廓等
# 您将看到以下功能：cv.findContours() ，cv.drawContours()

import cv2 as cv
import numpy as np

#如何找到二进制图像的轮廓 灰度图
img = cv.imread('./images/test.jpg')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
#第一个是源图像，第二个是轮廓检索模式，第三个是轮廓逼近方法。并输出轮廓和层次
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#如何绘制轮廓？
#只要有边界点，它也可以用来绘制任何形状。它的第一个参数是源图像，
# 第二个参数是应该作为Python列表传递的轮廓，
# 第三个参数是轮廓的索引(在绘制单个轮廓时很有用。要绘制所有轮廓，请传递-1)，
# 其余参数是颜色，厚度等等

#绘制所有轮廓
cv.drawContours(img, contours, -1, (0, 255, 0), 3)
#绘制单个轮廓
cv.drawContours(img, contours, 3, (0,255,0), 3)

# 轮廓特征
# 学习找到轮廓的不同特征，如区域，周长，边界矩形等。
#
# 目标
# 在本文中，我们将学习
#
# 查找轮廓的不同特征，例如面积，周长，质心，边界框等
# 您将看到大量与轮廓有关的功能。
