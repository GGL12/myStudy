# 目标
#
#     学习对图像的几种算术运算，如加法，减法，按位运算等。
#     您将学习以下函数：cv.add()，cv.addWeighted()等。
import numpy as np
import cv2 as cv

x = np.uint8([250])
y = np.uint8([10])
print(cv.add(x, y))

#图像混合
img_1 = cv.imread('./images/test.jpg')
img_2 = cv.imread('./images/copy_test.jpg')
dst = cv.addWeighted(img_1, 0.7, img_2, 0.3, 0)
img_1.shape
img_2.shape
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()