# 目标 图像阈值
#
# 在本教程中：
#
#     你会学到简单阈值法，自使用阈值法，以及 Otsu 阈值法等。
#     你会学到如下函数：cv.threshold，cv.adaptiveThreshold 等。
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('./images/test.jpg', 0)
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
#自适应阈值

img_2 = cv.imread('./images/test.jpg', 0)
img_2 = cv.medianBlur(img, 5)
ret, th1 = cv.threshold(img_2, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img_2, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img_2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
titles_2 = ['Original Image', 'Global Thresholding(v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images_2 = [img_2, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images_2[i], 'gray')
    plt.title(titles_2[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

#Otsu 二值化
#对于阈值，只需通过零。然后，该算法找到最佳阈值，并作为第二个输出返回 retval。如果不使用 otsu 阈值，则 retval 与你使用的阈值相同。

#全局阈值
ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
#Otsu阈值
ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
#经过高斯滤波的Otsu阈值
blur = cv.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()
