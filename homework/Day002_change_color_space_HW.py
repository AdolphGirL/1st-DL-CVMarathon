# -*- coding: utf-8 -*-

import os
import cv2


dir_path = os.pardir + os.path.sep + 'data' + os.path.sep + 'imgs'
img_path = os.path.join(dir_path, 'lena.png')
# print(img_path)

# 讀入RGB的資料
img = cv2.imread(img_path, cv2.IMREAD_COLOR)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hsl = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

while True:
    cv2.imshow('bgr', img)
    cv2.imshow('hsv', img_hsv)
    cv2.imshow('hsl', img_hsl)
    cv2.imshow('lab', img_lab)

    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break
