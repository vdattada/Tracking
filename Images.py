__author__ = 'Vijay'
from PIL import Image
import cv2

img = cv2.imread("C:\\Users\\Vijay\\Pictures\\aidan july 2010 pictures 003.jpg")

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.namedWindow("Features")
cv2.imshow('Features', hsvImg)

cv2.waitKey(0)
cv2.destroyAllWindows()