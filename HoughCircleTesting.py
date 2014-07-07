import cv2
import numpy as np
import time

shape = 0
thresh = 0

def nothing(x):
    pass

def on_trackbar(x):
    pass

cv2.namedWindow('Shapes')
#img = cv2.imread('img2.png')
img = cv2.imread('coins2.jpg')

cv2.createTrackbar('Lines/Circles', 'Shapes', 0, 1, on_trackbar)
cv2.createTrackbar('Acc Threshold', 'Shapes', 100, 300, on_trackbar)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

print str(shape)+ " " +str(thresh)
circles = cv2.HoughCircles(gray,cv2.cv.CV_HOUGH_GRADIENT,2,100,param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles, 0))

for i in circles[0,:]:
    #draw the outer circle
    cv2.circle(img,(i[0], i[1]), i[2], (0, 255, 0), 2)
    #draw the centre of the circle
    cv2.circle(img, (i[0], i[1]), 2, (255, 0, 255), 3)



while 1:
    shape = cv2.getTrackbarPos('Lines/Circles', 'Shapes')
    thresh = cv2.getTrackbarPos('Acc Threshold', 'Shapes')


    cv2.imshow('Shapes', img)
    cv2.imshow('Shapes1', gray)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
