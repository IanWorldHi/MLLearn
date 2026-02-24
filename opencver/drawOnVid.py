import cv2 as cv
import numpy as np


blank = np.zeros((500, 500, 3), dtype='uint8') #blank image, 500x500 pixels, uint8 means 0-255 for each pixel - img datatype
#3 is num of colour channels (rgb)
blank[:] = 0, 255, 0 #calls all of blank, setes it to rgb
blank[100:200, 100:200] = 200, 0, 0 #sets a portion to diff colour

cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), thickness=2) #text, position, font, size, colour, thickness
cv.circle(blank, (100, 50), 10, (0, 0, 255), thickness=-1) 
cv.line(blank, (0, 0), (250, 250), (255, 0, 0), thickness=3)
cv.rectangle(blank, (0, 0), (200, 200), (0, 0, 100), thickness=2) #or thickness=cv.FILLED or -1 to fill
# or blank.shape[0]//2 and blank.shape[1]//2 to set relative size

cv.imshow('nameOfWindow', blank)
cv.waitKey(0)




