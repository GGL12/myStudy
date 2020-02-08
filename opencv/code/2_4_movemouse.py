# 在本次会议中：
# 学习用 OpenCV 处理鼠标事件
# 你将学习这些函数：cv.setMouseCallback()
import cv2 as cv
events = [i for i in dir(cv) if 'EVENT' in i]
print(events)

import numpy as np
import cv2 as cv

def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)
img = np.zeros((512, 512, 3), np.int8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
while(1):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xff == 27:
        break
cv.destroyAllWindows()