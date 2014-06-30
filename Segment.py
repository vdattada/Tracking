from SimpleCV import Camera, Display, Image, HaarCascade

display = Display()
#lenna = Image("c:\\lenna.png")
#face = lenna.crop(200,200,200,200)
lenna = Image("C:\\Users\\Vijay\\Pictures\\aidan july 2010 pictures 008.jpg")


segment = HaarCascade("C:\\haarcascade_fullbody.xml")

autoface = lenna.findHaarFeatures(segment)
if ( autoface is not None ):
    face = autoface[-1].crop()


while display.isNotDone():
    face.show()