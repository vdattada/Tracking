from SimpleCV import Image, Display

disp = Display()
img = Image("C:\\Users\\Vijay\\Pictures\\aidan july 2010 pictures 012.jpg").resize(400, 500)
imgBin = img.binarize()
imgDilate = img.dilate(2)
imgErode = img.erode(2)

while disp.isNotDone():
    img.sideBySide(imgBin).sideBySide(imgDilate).sideBySide(imgErode).scale(0.5).show()



