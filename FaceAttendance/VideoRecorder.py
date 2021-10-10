# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 20:01:14 2017

"""


import matplotlib.pyplot as plt
import cv2

try:
    
    cap=cv2.VideoCapture(0)
    fourcc=cv2.VideoWriter_fourcc(*'DIVX')
    output=cv2.VideoWriter('C:\Users\Mohammad Bakir\Documents\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM/capture1.mp4',fourcc,15.0,(640,480),True)

    while(True):
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        output.write(hsv)
        cv2.resizeWindow('Cam',640,460)
        cv2.imshow('Cam',frame)
        if cv2.waitKey(1)==ord('q'):
            break
       
    cap.release()
    output.release()
    cv2.destroyAllWindows()
except:
    cap.release()
    output.release()
    cv2.destroyAllWindows() 
       
