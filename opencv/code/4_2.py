# 目标
#
# 在本教程中：
#
#     你将会学到将不同的几何变换应用于图像，如平移、旋转、仿射变换(一元线性变换)等。
#     另外，我们会创建一个从视频中提取彩色对象的应用。
#     你会学到如下函数：cv.getPerspectiveTransform

import numpy as np
import cv2 as cv

#比例
'''
比例是调整图片的大小。 OpenCV 使用 cv.resize() 函数进行调整。
可以手动指定图像的大小，也可以指定比例因子。可以使用不同的插值方法。
最好的插值方法是用于收缩的 cv.INTER_AREA 和 cv.INTER_CUBIC （慢）
和快速方法 cv.INTER_LINEAR 。默认情况下，所使用的插值方法都是 cv.INTER_AREA 。
你可以使用如下方法调整输入图片大小：
'''
img = cv.imread('./images/test.jpg')
res = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
cv.imshow('ori_img', img)
cv.imshow('result', res)
cv.waitKey(0)
cv.destroyAllWindows()

#变换
img = cv.imread('./images/test.jpg', 0)
rows, cols = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('img', dst)
cv.waitKey()
cv.destroyAllWindows()

#旋转 它将图像相对于中心旋转 90 度，而不进行任何缩放。
img = cv.resize(img, (80,60))
rows, cols = img.shape
#cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols -1) / 2.0, (rows-1)/2.0), 90, 1)
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('img', dst)
cv.waitKey()
cv.destroyAllWindows()

#仿射变换 y = ax + b 一元线性变换
from matplotlib import pyplot as plt
img = cv.imread('./images/test.jpg',1)
rows, cols, ch = img.shape
pts1 = np.float32([[50 ,50], [200, 50], [50, 200]])
pts2 = np.float32([[10 ,100], [200, 50], [100, 250]])
M = cv.getAffineTransform(pts1, pts2)
dst = cv.warpAffine(img, M, (cols, rows))
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()

#感知变换
# 对于感知转换，你需要一个 3x3 变换矩阵。即使在转换之后，直线也将保持直线。要找到这个变换矩阵，
# 需要输入图像上的 4 个点和输出图像上的相应点。在这四点中，有三点不应该共线。
# 然后通过 cv.getPerspectiveTransform 找到变换矩阵。
# 然后对这个 3x3 变换矩阵使用 cv.warpPerspective。
img = cv.imread('./images/test.jpg')
rows, cols, ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (300, 300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

