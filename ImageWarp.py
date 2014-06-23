from SimpleCV import Display, Camera, Image

tv_original = Image("C:\\Users\\Vijay\\Pictures\\aidan july 2010 pictures 012.jpg").resize(600,500).binarize()

tv_coordinates = [(100, 200),(400, 200),(400, 450), (100, 450)]
tv_mask = Image(tv_original.size()).invert().warp(tv_coordinates)
tv = tv_original - tv_mask

cam = Camera()
disp = Display(tv.size())

while disp.isNotDone():
    bwImage = cam.getImage().resize(tv.width, tv.height)
    on_tv = tv +bwImage.warp(tv_coordinates)
    on_tv.save(disp)