import numpy as np
import cv2 as cv

#opencv 读取图片 默认是彩色1，0为灰度图
img = cv.imread('./images/test.jpg', 0)
cv.imshow('image', img)
#waitKey是一个键盘绑定函数
cv.waitKey(0)
#摧毁窗口，destropWindows+具体的参数名
cv.destroyAllWindows()

#提前创建一个窗口是可以拖动的
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()

#保存图像
cv.imwrite('./images/copy_test.jpg', img)

#总结代码。按s保存，ese退出不保存
img_summary_first = cv.imread('./images/test.jpg', 0)
cv.imshow('Window_1', img)
#如果使用的是64位机器，则k = cv.waitKey(0) & 0xFF
k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('./images/save_iamge.jpg', img)
    cv.destroyAllWindows()

