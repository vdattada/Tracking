from SimpleCV import Camera, Display

cam = Camera()
display = Display()
rotate = 0
while display.isNotDone():
    rotate = rotate + 0.01
    cam.getImage().rotate(rotate).save(display)
