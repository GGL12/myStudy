# 平滑图像
# 目标
#
# 在本教程中：
#
#     用各种低通滤波器模糊图像。
#     对图像应用自定义过滤器（二维卷积）。

#二维卷积(图像滤波)
# 将该内核保持在一个像素之上，将该内核下面的所有 25 个像素相加，取其平均值，
# 并用新的平均值替换中心像素。它继续对图像中的所有像素执行此操作。尝试此代码并检查结果：
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('./images/test.jpg')
kernel = np.ones((5, 5), np.float32)/25
dst = cv.filter2D(img, -1, kernel)
plt.subplot(121)
plt.imshow(img)
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(dst)
plt.title('Averaging')
plt.xticks([])
plt.yticks([])
plt.show()

#图像模糊（图像平滑）

#1平均化
#这是通过用一个标准化的框过滤器卷积图像来完成的。它只需取内核区域下所有像素的平均值并替换中心元素。这是通过函数 **cv.blur()
img_3_1 = cv.imread('./images/test.jpg')
img_3_1 = img_3_1[:, :, [2, 1, 0]]

blur = cv.blur(img_3_1, (5, 5))

plt.subplot(121)
plt.imshow(img_3_1)
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(blur)
plt.title('Blurrde')
plt.xticks([])
plt.yticks([])
plt.show()
cv.imshow(img_3_1)

#高斯模糊
blur = cv.GaussianBlur(img,(5,5),0)

#中值滤波
median = cv.medianBlur(img,5)

#双边滤波
blur = cv.bilateralFilter(img,9,75,75)


