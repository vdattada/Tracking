from SimpleCV import Camera, Display, Image, Color, ColorMap

display = Display()
cam = Camera()

while display.isNotDone():

    img = cam.getImage().flipHorizontal()
    blobs = img.findBlobs()
    cm = ColorMap(Color.ORANGE,Color.WHITE,min(blobs.area()),max(blobs.area()))
    if blobs:
        for b in blobs:
            b.draw(cm[b.area()])

    img.show()
