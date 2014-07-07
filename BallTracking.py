import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
width,height = cap.get(3),cap.get(4)
print "frame width and height : ", width, height

iLowH = 0
iHighH = 179

iLowS = 0
iHighS = 255

iLowV = 0
iHighV = 255


cv2.namedWindow('frame')
cv2.namedWindow('frame1')
# create trackbars for color change
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

    # define range of blue color in HSV
    lower = np.array([iLh,iLs,iLv], dtype=np.uint8)
    upper = np.array([iHh,iHs,iHv], dtype=np.uint8)


    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Display the resulting frame
    cv2.inRange(hsv,lower,upper)
    el = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    hsv = cv2.erode(hsv,el,iterations=2)
    hsv = cv2.dilate(hsv,el,iterations=2)
    hsv = cv2.dilate(hsv,el,iterations=2)
    hsv = cv2.erode(hsv,el,iterations=2)

    gaussian_blur=cv2.GaussianBlur(hsv,(5,5),0)

    cv2.imshow('frame',hsv)
    cv2.imshow('frame1',frame)


    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()