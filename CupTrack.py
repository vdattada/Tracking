import SimpleCV
cam = SimpleCV.Camera(0, prop_set={"width": 656, "height": 492})

while True:
    img = cam.getImage().flipHorizontal()
    dist = img.colorDistance(SimpleCV.Color.ORANGE).dilate(2)
    segmented = dist.stretch(200,255)
    blobs = segmented.findBlobs()
    if blobs:
        circles = blobs.filter([b.isCircle(0.2) for b in blobs])
        if circles:
            img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(),SimpleCV.Color.BLUE,3)

    img.show()
