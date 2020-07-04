# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np


dir_path = os.pardir + os.path.sep + 'data' + os.path.sep + 'imgs'
img_path = os.path.join(dir_path, 'lena.png')
# print(img_path)

# HSL改變飽和度
change_percentage = 0.1
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img_hsl = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

# cv2順序HLS，先降低飽和度
img_hsl_down = img_hsl.astype('float32')
img_hsl_down[:, :, 2] = img_hsl_down[:, :, 2] / 255 - change_percentage
# 降低飽和度後，小於0的設定為0，邊緣處理
img_hsl_down[img_hsl_down[:, :, 2] < 0] = 0
# 轉回BGR(另一種寫法)
img_hsl_down[..., -1] = img_hsl_down[..., -1] * 255
img_hsl_down = img_hsl_down.astype('uint8')
img_hsl_down = cv2.cvtColor(img_hsl_down, cv2.COLOR_HLS2BGR)

#  增加飽和度
img_hsl_up = img_hsl.astype('float32')
img_hsl_up[..., -1] = img_hsl_up[..., -1] / 255 + change_percentage
img_hsl_up[img_hsl_up[..., -1] > 1] = 1
img_hsl_up[..., -1] = img_hsl_up[..., -1] * 255
img_hsl_up = img_hsl_up.astype('uint8')
img_hsl_up = cv2.cvtColor(img_hsl_up, cv2.COLOR_HLS2BGR)

img_all = np.hstack((img, img_hsl_down, img_hsl_up))
while True:
    cv2.imshow('result', img_all)

    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break

# 灰階直方圖均化，改變明亮和對比
img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img_gray_equalHist = cv2.equalizeHist(img_gray)
img_all = np.hstack((img_gray, img_gray_equalHist))
while True:
    cv2.imshow('result', img_all)

    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break

# 手動調整對比和明亮
# 對比
img_contrast = cv2.convertScaleAbs(img, alpha=2.0, beta=0)
# 明亮加強
img_light = cv2.convertScaleAbs(img, alpha=1.0, beta=50)
img_all = np.hstack((img, img_contrast, img_light))
while True:
    cv2.imshow('result', img_all)

    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break