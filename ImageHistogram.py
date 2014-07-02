from SimpleCV import Image, Camera, Display
import matplotlib.pyplot as plt

img = Image('simplecv')
gray = img.toGray()
histogram = gray.histogram(255)
print len(histogram)
print histogram
plt.plot(histogram)
plt.show()