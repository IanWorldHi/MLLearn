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

if img is not None:
    cv.imshow('nameOfWindow', img)


#contours
#They are the boundaries of objects 

cv.waitKey(0)


