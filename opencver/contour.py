import cv2 as cv
import numpy as np

img = cv.imread('photosOpenCvEx/Screenshot_20230120_050930.png')

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img, scale=0.5)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
""" img = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
img = cv.Canny(img, 75, 125)  """

#alt way of procesing for contours - thresholds to black and white pixels (THRESH_BINARY)
ret, thresh = cv.threshold(img, 125, 255, cv.THRESH_BINARY)


#contours, hierachies = cv.findContours(img, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) #retrieval mode, contour approximation method
contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contours, -1, 255, 1) #-1 = draw all contours, color(just one here cuz its grayed), thickness of line

if img is not None:
    cv.imshow('blank', blank)
    #cv.imshow('nameOfWindow', img)
    cv.imshow('nameOfWindow2', thresh)


#contours
#They are the boundaries of objects 

cv.waitKey(0)

#print(f'{img} lets see')



