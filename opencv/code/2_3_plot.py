# 在本次会议中：
# # # # 用 OpenCV 画不同的几何图形
# # # # 你要学习这些函数：cv.line(), cv.circle() , cv.rectangle(), cv.ellipse(), cv.putText() 等。

#画线
import numpy as np
import cv2 as cv
# 创建一个黑色的图像
img = np.zeros((512,512,3), np.uint8)
# 画一条 5px 宽的蓝色对角线
cv.line(img,(0,0),(511,511),(255,0,0),5)

#画矩形
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
#画圆
cv.circle(img,(447,63), 63, (0,0,255), -1)
#画椭圆
cv.ellipse(img, (256,256),(100,50),0,0,180,255,-1)

#画多边形
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

#添加文字:图片,文字，位置，字体类型，字体大小，字体颜色，字体粗细
cv.putText(img, "guolei", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 20, (0, 0, 255), 2)
cv.imshow('show', img)
cv.waitKey(0)
cv.destroyAllWindows()