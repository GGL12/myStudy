# 目标
#
# 在本教程中：
#
#     你会学到如何将图片从一个颜色空间转换到另一个，例如 BGR 到 Gray，BGR 到 HSV 等。
#     另外，我们会创建一个从视频中提取彩色对象的应用。
#     你会学到如下函数：cv.cvtColor()，cv.inRange()

#改变颜色空间
import cv2 as cv
colors_floags = [i for i in dir(cv) if i.startswith('COLOR_')]
print(len(colors_floags))
#cv.cvtColor(input_image, flag) 'COLOR_BAYER_BG2BGR', 'COLOR_BAYER_BG2BGRA',

#目标追踪

# 现在我们知道了如何将 BGR 图片转化为 HSV 图片，我们可以使用它去提取彩色对象。HSV 比 BGR 在颜色空间上更容易表示颜色。在我们的应用中，我们会尝试提取一个蓝色的彩色对象，方法为：
#
#     提取每一视频帧。
#     将 BGR 转化为 HSV 颜色空间。
#     我们将 HSV 图片的阈值设为蓝色范围。
#     现在提取出了蓝色对象，我们可以随意处理图片了
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # 定义蓝色在hsv的范围 https://blog.csdn.net/taily_duan/article/details/51506776
    # lower_blue = np.array([100,43,46])
    # upper_blue = np.array([124,255,255])
    lower_blue = np.array([0,43,46])
    upper_blue = np.array([10,255,255])
    #得到白色轮廓
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # 与原始图像与运算
    #res得到蓝色
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()

#如何找到HSV值去追踪目标
green = np.uint8([[[0, 255, 0]]])
hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
print(hsv_green)
#现在你可以取 [H-10, 100,100] 和 [H+10, 255, 255] 分别作为上界和下界.
# 除此之外，你可以使用任何图像编辑工具（如 GIMP）或任何在线转换器来查找这些值，
# 但不要忘记调整 HSV 范围。
