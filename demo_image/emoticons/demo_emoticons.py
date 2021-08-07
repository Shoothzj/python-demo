import sys

import cv2
import matplotlib.pyplot as plt


# 绘图函数
def plt_show(img):
    imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imageRGB)
    plt.show()


# 导入灰度图即可
image = cv2.imread(sys.argv[1], 0)
plt_show(image)

# 因为我们发现前景照片的尺寸比背景尺寸还要大，这显然是不合适的，所以要先对其进行等比例（0.3）缩放。
image_resize = cv2.resize(image, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_CUBIC)
plt_show(image_resize)

# 在这里，我们将像素值大于 80 的区域设置为 255；小于 80 的区域设置成 0。
ret, image_binary = cv2.threshold(image_resize, 80, 255, cv2.THRESH_BINARY)
plt_show(image_binary)

foreground = image_binary