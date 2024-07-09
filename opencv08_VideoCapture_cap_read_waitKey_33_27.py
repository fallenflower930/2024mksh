# -*- coding: utf-8 -*-
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    cv2.imshow('opencv08', img)
    if cv2.waitKey(33)==(27):
        break
    
cv2.destroyAllWindows()    

