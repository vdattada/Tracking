from SimpleCV import Image, Display

disp = Display()
img = Image("C:\\jacopo.jpg").resize(250, 300)
otsu = img.binarize()
low = img.binarize(75)
high = img.binarize(125)

top = img.sideBySide(otsu)
bottom = low.sideBySide(high)
combined = top.sideBySide(bottom, side='bottom')

while disp.isNotDone():
    combined.show()


