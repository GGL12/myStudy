# 形态转化
# 在本教程中：
#
#     我们将学习不同的形态操作，如腐蚀、扩张、开、闭等。
#     我们将看到不同的函数，如： cv.erode()、 cv.dilate()、 **cv.morphologyEx()**等。

#1 腐蚀
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('./images/test.jpg')
blur = cv.blur(img, (5, 5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#扩张
kernel = np.ones((5, 5))
dilation = cv.dilate(img, kernel, iterations=1)

#开
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

#闭
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

#形态梯度
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

#顶帽
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)

#黑帽
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

#结构参量
#矩形
cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
#椭圆
cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
#十字形
cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
