# -*- coding: utf-8 -*-

import cv2
import os

dir_path = os.pardir + os.path.sep + 'data' + os.path.sep + 'imgs'
img_path = os.path.join(dir_path, 'lena.png')

img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

while True:
    cv2.imshow('bgr', img)
    cv2.imshow('gray', img_gray)

    # 直到按下 ESC 鍵才會自動關閉視窗結束程式
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break
