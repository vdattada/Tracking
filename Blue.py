import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')

iLowH = 0
iHighH = 179

iLowS = 0
iHighS = 255

iLowV = 0
iHighV = 255

cv2.createTrackbar('iLowH', 'frame', iLowH, iHighH, nothing)
cv2.createTrackbar('iHighH', 'frame', iLowH, iHighH, nothing)

cv2.createTrackbar('iLowS', 'frame', iLowS, iHighS, nothing)
cv2.createTrackbar('iHighS', 'frame', iLowS, iHighS, nothing)

cv2.createTrackbar('iLowV', 'frame', iLowV, iHighV, nothing)
cv2.createTrackbar('iHighV', 'frame', iLowV, iHighV, nothing)

while(1):
    iLh = cv2.getTrackbarPos('iLowH','frame')
    iLs = cv2.getTrackbarPos('iLowS','frame')
    iLv = cv2.getTrackbarPos('iLowV','frame')

    iHh = cv2.getTrackbarPos('iHighH','frame')
    iHs = cv2.getTrackbarPos('iHighS','frame')
    iHv = cv2.getTrackbarPos('iHighV','frame')

    # Take each frame
    retVal, frame = cap.read()

    frame = cv2.flip(frame, 1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.medianBlur(gray, 5)

    # define range of blue color in HSV
    lower = np.array([iLh, iLs, iLv], dtype=np.uint8)
    upper = np.array([iHh, iHs, iHv], dtype=np.uint8)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower, upper)

    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame, frame, mask=mask)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    '''
    circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 2, 50, param1=200, param2=100, minRadius=25, maxRadius=100)

    if circles is None:
            continue
    #print circles

    circles = np.uint16(np.around(circles, 0))

    for i in circles[0,:]:
        #draw the outer circle
        cv2.circle(frame,(i[0], i[1]), i[2], (0, 255, 0), 2)
        #draw the centre of the circle
        cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
    '''
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    #cv2.imshow('gray', gray)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()