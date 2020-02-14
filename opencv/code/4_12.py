# 模板匹配
# # 目标
# # 在本章中，您将学习
# #
# # 使用模板匹配查找图像中的对象
# # 您将了解这些函数： cv.matchTemplate（） ， cv.minMaxLoc（）

# 理论
# 模板匹配是一种在较大图像中搜索和查找模板图像位置的方法。为此，OpenCV 带有一个函数 cv.matchTemplate（） 。
# 它只是在输入图像上滑动模板图像（如在 2D 卷积中），并比较模板图像下的模板和输入图像的补丁。
# 在 OpenCV 中实现了几种比较方法。 （您可以查看文档以获取更多详细信息）。
# 它返回一个灰度图像，其中每个像素表示该像素的邻域与模板匹配的程度。
#
# 如果输入图像的大小（WxH）且模板图像的大小（wxh），则输出图像的大小为（W-w + 1，H-h + 1）。
# 得到结果后，可以使用 cv.minMaxLoc（） 函数查找最大/最小值的位置。
# 将其作为矩形的左上角，取（w，h）作为矩形的宽度和高度。那个矩形是你的模板区域
