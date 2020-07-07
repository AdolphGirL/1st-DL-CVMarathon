# -*- coding: utf-8 -*-


import os
import cv2
import numpy as np
import time


"""
翻轉：實作上下翻轉、[h, w, c]，[高 寬 通道]
縮放：實作鄰近差值
平移：建立 Translation Transformation Matrix 來做平移
"""


def show_img(img):
    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(0)
        if k == 27:
            cv2.destroyAllWindows()
            break


dir_path = os.path.pardir + os.path.sep + 'data' + os.path.sep + 'imgs'
img_path = os.path.join(dir_path, 'lena.png')

org_img = cv2.imread(img_path, cv2.IMREAD_COLOR)

# 垂直翻轉 (vertical)
img_v_flip = org_img[::-1, :, :]
v_flip = np.hstack((org_img, img_v_flip))
show_img(v_flip)

# 水平翻轉 (horizontal)
img_h_flip = org_img[:, ::-1, :]
h_flip = np.hstack((org_img, img_h_flip))
show_img(h_flip)

# 水平 + 垂直翻轉
img_hv_flip = org_img[::-1, ::-1, :]
hv_flip = np.hstack((org_img, img_hv_flip))
show_img(hv_flip)

# 縮小圖片
img_scale_small = cv2.resize(org_img, None, fx=0.2, fy=0.2)
# show_img(img_scale_small)

# 將圖片放大為"小圖片"的 8 倍大 = 原圖的 1.6 倍大
fx, fy = 8, 8

# 鄰近差值 cv2.INTER_NEAREST
start_time = time.time()
img_area_scale = cv2.resize(img_scale_small, None, fx=fx, fy=fy, interpolation=cv2.INTER_NEAREST)
print('INTER_NEAREST zoom cost {}'.format(time.time() - start_time))

# 雙立方差補 cv2.INTER_CUBIC
start_time = time.time()
img_cubic_scale = cv2.resize(img_scale_small, None, fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
print('INTER_CUBIC zoom cost {}'.format(time.time() - start_time))

img_zoom = np.hstack((img_area_scale, img_cubic_scale))
show_img(img_zoom)

# x 平移 100 pixel; y 平移 50 pixel
M = np.array([
    [1, 0, 100],
    [0, 1, 50]
], dtype=np.float32)

shift_img = cv2.warpAffine(org_img, M, (org_img.shape[1], org_img.shape[0]))
show_img(shift_img)


