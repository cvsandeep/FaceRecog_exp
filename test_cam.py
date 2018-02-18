# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 21:22:43 2018

@author: cvssa
"""

import cv2
cam = cv2.VideoCapture(0)

s, img = cam.read()
if s:    # frame captured without any errors
    cv2.namedWindow("cam-test", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("cam-test",img)
    cv2.waitKey(0)
    cv2.destroyWindow("cam-test")
    cv2.imwrite("C://filename.jpg",img) #save image
    

