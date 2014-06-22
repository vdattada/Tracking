__author__ = 'Vijay'

import cv2
import numpy as np


print cv2.__version__
img = cv2.imread('C:\\Users\\Vijay\\Pictures\\aidan july 2010 pictures 003.jpg')
height, width = img.shape[:2]
print height
print width

res = cv2.resize(img,(width/4, height/4), interpolation = cv2.INTER_CUBIC)
while(1):
    cv2.imshow("Test", res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break