import cv2
import numpy as np

def getthresholdedimg(hsv):
    yellow = cv2.inRange(hsv,np.array((20,100,100)),np.array((38,255,255)))
    blue = cv2.inRange(hsv,np.array((75,100,100)),np.array((130,255,255)))
    green= cv2.inRange(hsv,np.array((32,42,120)),np.array((75,255,255)))
    red = cv2.inRange(hsv,np.array((160,100,47)),np.array((179,255,255)))
    #both = cv2.add(green,blue)
    both = yellow+blue+green+red
    return both

c = cv2.VideoCapture(0)
width,height = c.get(3),c.get(4)
print "frame width and height : ", width, height

while(1):
    _,f = c.read()
    f = cv2.flip(f,1)

    blur = cv2.medianBlur(f,5)
    hsv = cv2.cvtColor(f,cv2.COLOR_BGR2HSV)

    both = getthresholdedimg(hsv)

    erode = cv2.erode(both,None,iterations = 3)
    dilate = cv2.dilate(erode,None,iterations = 10)

    #cv2.imshow('',dilate)
    contours,hierarchy = cv2.findContours(dilate,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cx,cy = x+w/2, y+h/2
        print "cx:"+str(cx)+" cy:"+str(cy)+ " hsv:"+str(hsv.item(cy,cx,0))

        if 5 < hsv.item(cy,cx,0) < 30:
            cv2.rectangle(f,(x,y),(x+w,y+h),[0,255,255],2)
            print "yellow :", x,y,w,h
        elif 30 < hsv.item(cy,cx,0) < 76:
            cv2.rectangle(f,(x,y),(x+w,y+h),[0,255,0],2)
            print "green :", x,y,w,h
        elif 100 < hsv.item(cy,cx,0) < 120:
            cv2.rectangle(f,(x,y),(x+w,y+h),[255,0,0],2)
            print "blue :", x,y,w,h
        elif 150 < hsv.item(cy,cx,0) < 180:
            cv2.rectangle(f,(x,y),(x+w,y+h),[0,0,255],2)
            print "red :", x,y,w,h


    cv2.imshow('img',f)

    if cv2.waitKey(25) == 27:
        break

c.release()
cv2.destroyAllWindows()
