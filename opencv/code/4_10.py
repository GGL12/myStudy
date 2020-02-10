# 学习直方图的基础知识
# #
# # 目标
# # 学会
# #
# # 使用OpenCV和Numpy函数查找直方图
# # 使用OpenCV和Matplotlib函数绘制直方图
# # 您将看到以下功能：cv.calcHist() ，np.histogram() 等。

# 1. OpenCV中的直方图计算
# 因此，现在我们使用 cv.calcHist() 函数查找直方图。让我们熟悉一下函数及其参数：

# images：它是uint8或float32类型的源图像。它应该放在方括号中，即“ [img]”。
# channels：也以方括号给出。它是我们计算直方图的通道的索引。例如，如果输入为灰度图像，则其值为[0]。对于彩色图像，您可以传递[0]，[1]或[2]分别计算蓝色，绿色或红色通道的直方图。
# mask：遮罩图像。为了找到完整图像的直方图，将其指定为“无”。但是，如果要查找图像特定区域的直方图，则必须为此创建一个遮罩图像并将其作为遮罩。(我将在后面显示一个示例。)
# histSize：这表示我们的BIN计数。需要放在方括号中。对于全尺寸，我们通过[256]。
# ranges：这是我们的RANGE。通常为[0,256]。 因此，让我们从示例图像开始。只需在灰度模式下加载图像并找到其完整的直方图即可。
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('./images/test.jpg', 0)
hist = cv.calcHist([img], [0], None,[256], [0, 256])
#plt.imshow(img[:, :, [2, 1, 0]])
plt.show()

# 2. Numpy中的直方图计算
# Numpy还为您提供了一个函数 np.histogram() 。因此，您可以在下面的行尝试代替 calcHist() 函数：
hist, bins = np.histogram(img.ravel(), 256, [0,256])

#绘制直方图
# 有两种方法，
#
# 简短方法：使用Matplotlib绘图功能
# 很长的路要走：使用OpenCV绘图功能
img = cv.imread('./images/test.jpg', 0)
plt.hist(img.ravel(), 256, [0,256])
plt.show()

img = cv.imread('./images/test.jpg')
color = ('b', 'g', 'r')
for i,col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(histr, color=col)
    plt.xlim([0,256])
plt.show()

# 2.使用OpenCV
# 好吧，在这里您可以调整直方图的值及其bin值，使其看起来像x，y坐标，
# 以便可以使用 cv.line() 或 cv.polyline() 函数绘制它以生成与上述相同的图像。
# OpenCV-Python2官方示例已经提供了此功能。检查 samples/python/hist.py 代码