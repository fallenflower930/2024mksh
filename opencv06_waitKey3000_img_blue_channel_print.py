# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('mksh.jpg')
b = img[:,:,0]#blue channel
print(b)
cv2.imshow('opencv06', img)
cv2.waitKey(3000)#等按空白
#等三秒無按鍵就離開
cv2.destroyAllWindows()#再關視窗
