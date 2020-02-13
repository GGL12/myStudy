# 在本节中，我们将学习
#
# 使用OpenCV查找图像的傅立叶变换
# 利用Numpy中可用的FFT功能
# 傅立叶变换的一些应用
# 我们将看到以下函数：cv.dft() ，cv.idft() 等


#Numpy中的傅立叶变换
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('./images/test.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))
plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Input Image')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')
plt.xticks([])
plt.yticks([])
plt.show()

#OpenCV中的傅立叶变换
# OpenCV 为此提供了功能 cv.dft() 和 cv.idft() 。它返回与以前相同的结果，但是有两个通道。
# 第一个通道将具有结果的实部，第二个通道将具有结果的虚部。输入的图像应首先转换为np.float32 。
# 我们将看到如何做。
img_opencv = cv.imread('./images/test.jpg', 0)
dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()