# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('RGB.png')
img = cv2.resize(img,(300,300))
cv2.imshow('RGB',img)

img1 = cv2.applyColorMap(img, cv2.COLORMAP_AUTUMN)
img2 = cv2.applyColorMap(img, cv2.COLORMAP_SPRING)
img3 = cv2.applyColorMap(img, cv2.COLORMAP_WINTER)


cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)

cv2.waitKey(0)

cv2.destroyAllWindows()
