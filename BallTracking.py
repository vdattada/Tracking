from SimpleCV import Color, Image
import time

img = Image("mandms-dark.png")
blue_distance = img.hueDistance(Color.LEGO_BLUE).invert()
blobs = blue_distance.findBlobs()
blobs.draw(color=Color.BLUE, width=2)
img.addDrawingLayer(blue_distance.dl())
img.show()
time.sleep(15)