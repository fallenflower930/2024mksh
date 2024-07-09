# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('RGB.png')
img = cv2.resize(img,(300,300))
cv2.imshow('RGB',img)

for i in range(20):
    img1 = cv2.applyColorMap(img, i)
    cv2.imshow('img'+str(i),img1)

cv2.waitKey(0)

cv2.destroyAllWindows()
