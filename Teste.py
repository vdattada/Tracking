from SimpleCV import *
import time
import numpy


class Track:
    def __init__(self):
        self.color = (0, 0, 0)
        self.blobs = []
        self.matched_blob_list = []

def get_overlap_area(minx1, miny1, maxx1, maxy1, minx2, miny2, maxx2, maxy2):
    if minx1 > maxx2 or maxx1 < minx2 or miny1 > maxy2 or maxy1 < miny2:
        return 0
    else:
        return (min(maxx2, maxx1) - max(minx2, minx1)) * (min(maxy2, maxy1) - max(miny2, miny1))

cam = Camera(0)

tracks = []
overlap_th = 100  # minimum overlap area for matching 

# Define criteria for blob analysis. 
tolerance = 0.3
min_blob_size = 100

while True:
    img = cam.getImage()

    # If you're not using Lenovo Y330, comment the line below out. 
    #img = img.flipVertical().flipHorizontal()
    
    # Extract blue pixles then binarize it. 
    blue_stuff = img.colorDistance(Color.BLUE)
    bin_blue_stuff = blue_stuff.binarize(130)
    
    # Remove noise using morphological opening then closing operation. 
    clean_bin_blue_stuff = bin_blue_stuff.morphOpen().morphClose()
    blobs = clean_bin_blue_stuff.findBlobs()

    # Check if there are blobs detected. 
    if blobs:
        # If there is no track yet, then create a new one. 
        if not tracks:
            for b in blobs:
                if b.isCircle(tolerance) and b.area() > min_blob_size:
                    t = Track()
                    t.color = Color().getRandom()
                    t.blobs.append(b)
                    tracks.append(t)
        else:
            # Construct an overlap area association matrix. 
            matrix = numpy.zeros((len(tracks), len(blobs)))
            for i in range(len(tracks)):
                last_blob_idx = len(tracks[i].blobs) - 1
                for j in range(len(blobs)):
                    matrix[i][j] = get_overlap_area(
                        tracks[i].blobs[last_blob_idx].minX(), 
                        tracks[i].blobs[last_blob_idx].minY(), 
                        tracks[i].blobs[last_blob_idx].maxX(), 
                        tracks[i].blobs[last_blob_idx].maxY(), 
                        blobs[j].minX(), blobs[j].minY(), 
                        blobs[j].maxX(), blobs[j].maxY())

            # Perform forward tracking. 
            for i in range(len(tracks)):
                tracks[i].matched_blob_list = []
                matched_blob_list = []
                for j in range(len(blobs)):
                    if matrix[i][j] >= overlap_th:
                        matched_blob_list.append(j)
                if len(matched_blob_list) == 1:
                    tracks[i].matched_blob_list.append(matched_blob_list[0])

            # Perform backward tracking. 
            unmatched_blob_list = []
            for j in range(len(blobs)):
                if blobs[j].isCircle(tolerance) and blobs[j].area() > min_blob_size:
                    matched_track_list = []
                    num_zero = 0
                    for i in range(len(tracks)):
                        if matrix[i][j] >= overlap_th:
                            matched_track_list.append(i)
                        elif matrix[i][j] == 0:
                            num_zero = num_zero + 1
                    if len(matched_track_list) == 1:
                        if j in tracks[matched_track_list[0]].matched_blob_list:
                            tracks[matched_track_list[0]].blobs.append(blobs[j])
                    if num_zero == len(tracks):
                        unmatched_blob_list.append(j)

            # Create new tracks for unmatched blobs. 
            for idx in unmatched_blob_list:
                t = Track()
                t.color = Color().getRandom()
                t.blobs.append(blobs[idx])
                tracks.append(t)

    # Draw a bounding box for each track. 
    for t in tracks:
        last_blob_idx = len(t.blobs) - 1
        layer = DrawingLayer((img.width, img.height))
        rect_dim = (t.blobs[last_blob_idx].width(), 
                    t.blobs[last_blob_idx].height())
        center = t.blobs[last_blob_idx].center()
        layer.centeredRectangle(center, rect_dim, t.color, 5)
        img.addDrawingLayer(layer)
    
    img.applyLayers()
    img.show()
    time.sleep(10)