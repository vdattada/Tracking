'''
__author__ = 'Vijay'
from SimpleCV import Image

#img=Image('logo')
img = Image('C:\\Users\\Vijay\\Downloads\\image1.jpg')
blobs = img.findBlobs(254.9)
print (blobs)

from SimpleCV import Camera, Display, Image
import time

cam0 = Camera(0, prop_set={"width": 1280, "height": 720})
cam1 = Camera(1, prop_set={"width": 1280, "height": 720})


#while True:
img0 = cam0.getImage()
img1 = cam1.getImage()
display = Display()

img0.drawText("Hello World 0")
img0.show()
img0.save('c:\\img0.png')

img1.drawText("Hello World 1")
img1.show()
img1.save('c:\\img1.png')

from SimpleCV import Camera, Display, Image, Color

winSize = (640,480)
display = Display(winSize)

img = Image(winSize)
img.save(display)

while not display.isDone():
    if display.mouseLeft:
        img.dl().circle((display.mouseX, display.mouseY), 9, Color.WHITE, filled=True)
        img.save(display)
        img.save("c:\\painting.png")

from SimpleCV import Camera, Image
import time

cam = Camera()
numframes = 6

for x in range(0, numframes):
    img = cam.getImage()
    filepath = "c:\\image-"+str(x)+".jpg"
    img.save(filepath)
    print "Saved image to: "+filepath

    time.sleep(5)
'''

from SimpleCV import Image
import time

img = Image('c:\\jacopo.jpg')
pixel = img[120,150]
img[120,150] = (255,0,0)
pixel = img[120,150]
print pixel
distance = img.colorDistance(img.getPixel(120,150))
distance.show()
bigImg = img.scale(4)
bigImg.show()
#img.show()

#blobs = img.findBlobs()
#print blobs.count(10)
#blobs[-1].crop().show()
time.sleep(10)