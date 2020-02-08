# 访问像素值并修改它们
# 访问像素属性
# 设置感兴趣区域（ROI）
# 拆分和合并图像

import numpy as np
import cv2 as cv
img = cv.imread('./images/test.jpg',)
h, w, c = img.shape

#OpenCV的读取顺序为B，G，R，由于图像所有像素为黄色，因此，G=255，R=255
img[100, 100] #array([90, 94, 89], dtype=uint8) 此点的三个通道值
blue = img[100, 100][0]
print(blue)
#可以使用这种方法修改像素值
img[100, 100] = [255, 255, 255]
print(img[100, 100])

#Numpy 是一个用于快速阵列计算的优化库。因此，简单地访问每个像素值并对其进行修改将非常缓慢，并不鼓励这样做
# 注意 上述方法通常用于选择数组的某个区域，比如前 5 行和后 3 列。对于单个像素的访问，
# # 可以选择使用 Numpy 数组方法中的 array.item()和 array.itemset()，注意它们的返回值是一个标量。
# # 如果需要访问所有的 G、R、B 的值，则需要分别为所有的调用 array.item()。

#访问BGR的值
img.item(100, 100, 1)
#修改通道的值
img.itemset((100, 100, 1), 100)
img.item(100, 100, 1)

#图像中感兴趣区域
ball = img[280:340, 330:390]

#拆分和合并图像通道
b_1, g, r = cv.split(img)
b_2 = img[:, :, 0]
b_1 == b_2
img[:, :, 0] = 0
#值作图像边框（填充）
# 如果要在图像周围创建边框，比如相框，可以使用 cv.copyMakeBorder()。但它有更多卷积运算，零填充等应用。该函数采用以下参数：
# src-输入的图像
# top,bottom,left,right-上下左右四个方向上的边界拓宽的值
# borderType-定义要添加的边框类型的标志。它可以是以下类型：
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
BLUE = [255,0,0]
img1 = cv.imread('opencv-logo.png')
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()

