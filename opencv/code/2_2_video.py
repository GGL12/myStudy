import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if cap.isOpened():
    while(True):
        #一帧一帧捕获
        ret, frame = cap.read()
        #对帧进行操作
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(1) & 0XFF ==ord('q'):
            break
cap.release()
cv.destroyAllWindows()

#保存视频
save_cap = cv.VideoCapture(0)
#声明编码器和创建VideoWrite 对象
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('./images/output.avi', fourcc, 20.0, (640, 480))
while(save_cap.isOpened()):
    ret, frame = save_cap.read()
    if ret:
        frame = cv.flip(frame, 0)
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break
save_cap.release()
out.release()
cv.destroyAllWindows()



