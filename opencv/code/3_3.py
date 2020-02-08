# 在图像处理中，由于我们每秒需要处理大量操作，因此我们的代码不仅要提供正确的解决方案，还要以最快的方式提供。所以，在本章中，我们将学习
#
#     衡量代码的性能
#     一些提高代码性能的技巧
#     我们将看到以下函数：cv.getTickCount,cv.getTickFrequency等。

import cv2 as cv
import numpy as np

e1 = cv.getTickCount()
#执行你的代码
e2 = cv.getTickCount()
time = (e2 - e1) / cv.getTickFrequency()

img1 = cv.imread('./images/test.jpg')
e1 = cv.getTickCount()
for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1, i)
e2 = cv.getTickCount()
t = (e2 - e1) / cv.getTickFrequency()
print(t)

#OpenCV 中的默认优化
cv.useOptimized()