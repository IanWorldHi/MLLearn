import cv2 as cv
import numpy as np

img = cv.imread('photosOpenCvEx/Screenshot_20230120_050956.png')

#colour spaces, just cv.cvtColor(img, cv.COLOR_BGR2HSV) or LAB, RGB etc

#colour channel, each of R, G and B are colour channels, mix or split em

if img is not None:
    width = int(img.shape[1] * 0.5)
    height = int(img.shape[0] * 0.5)
    dimensions = (width, height)
    img = cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
    b,g,r = cv.split(img) 
    merged = cv.merge([b,g,r])
    #cv.imshow('nameOfWindow', b) #shown as grayed
    #cv.imshow('nameOfWindow2', img)
    #cv.imshow('nameOfWindow3', merged)
    
    blank = np.zeros(img.shape[:2], dtype='uint8')
    blue = cv.merge([b, blank, blank])
    cv.imshow('nameOfWindow4', blue)
    
    print(img.shape)
    print(b.shape)
    

cv.waitKey(0)
