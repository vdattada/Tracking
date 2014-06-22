__author__='Vijay'
'''
import cv2
import sys
import numpy as np

img = cv2.imread("C:\\Users\\Vijay\\Pictures\\aidan july 2010 pictures 003.jpg", cv2.CV_LOAD_IMAGE_COLOR)  ## Read image file

if img is None:                      # Check for invalid input
    print "Could not open or find the image"
else:
    cv2.namedWindow('Display Window')        ## create window for display
    cv2.imshow('Display Window',img)         ## Show image in the window
    print "size of image: ",img.shape        ## print size of image
    cv2.waitKey(0)                           ## Wait for keystroke
    cv2.destroyAllWindows()                  ## Destroy all windows
'''
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
