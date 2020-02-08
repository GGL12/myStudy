# Canny 边缘检测
# 目标
# 在本章中，我们将了解
#
# Canny 边缘检测的概念
# OpenCV 的功能： cv.Canny（）
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('./images/test.jpg',0)
edges = cv.Canny(img, 20, 200)
plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(edges, cmap='gray')
plt.title('Edge Image')
plt.xticks([])
plt.yticks([])
plt.show()

