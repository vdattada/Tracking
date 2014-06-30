from SimpleCV import Camera, Display, ColorCurve, Image

screenSize = (640, 480)
rCurve = ColorCurve([[0,0],[64,64],[128,128],[256,128]])
gbCurve = ColorCurve([[0,16],[64,72],[128,148],[256,256]])

cam = Camera(-1,{'width':screenSize[0], 'height':screenSize[1]})
disp = Display(screenSize)


while not disp.isDone():
    img = cam.getImage()
    coloredImg = img.applyRGBCurve(rCurve,gbCurve,gbCurve)
    erodedImg = coloredImg.erode(1)
    erodedImg.save(disp)
    erodedImg.sideBySide(coloredImg)