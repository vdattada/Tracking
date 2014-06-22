__author__ = 'Vijay'
import cv2
import numpy as np

filename = 'C:\\Users\\Vijay\\Pictures\\aidan july 2010 pictures 003.jpg'
img = cv2.imread(filename)
height, width = img.shape[:2]
res = cv2.resize(img,(width/4, height/4), interpolation = cv2.INTER_CUBIC)

gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst, None)

# Threshold for an optimal value, it may vary depending on the image.
res[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',res)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
