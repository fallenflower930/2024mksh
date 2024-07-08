# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('onepiece.png')
b = img[:,:,0]# 冒號, 冒號,0 藍色
g = img[:,:,1]# 冒號, 冒號,1 綠色
r = img[:,:,2]# 冒號, 冒號,2 紅色

img_rbb = cv2.merge([r,b,b])
cv2.imshow('RBB', img_rbb)
#cv2.imshow('opencv02', img)
#cv2.imshow('blue', b)
#cv2.imshow('green', b)
#cv2.imshow('red', b)

cv2.waitKey(0)



