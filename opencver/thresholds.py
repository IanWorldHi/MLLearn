import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photosOpenCvEx/Screenshot_20230120_051143.png')

#Thresholding = binary realization of image


if img is not None:
    blank = np.zeros(img.shape[:2], dtype='uint8')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    #Simple Thresholding
    threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
    #img, threshold value, max value, type of thresholding (binary, binary inv, trunc, tozero, tozero inv)
    #returns: thresh = binarized image, threshold = same threshold value so 150
    
    
    #Adaptive Thresholding - has diff threshold for diff parts of the image/lighting
    
    img = cv.resize(img, (int(img.shape[1] * 0.3), int(img.shape[0] * 0.3)), interpolation=cv.INTER_AREA)
    thresh = cv.resize(thresh, (int(thresh.shape[1] * 0.3), int(thresh.shape[0] * 0.3)), interpolation=cv.INTER_AREA)
    
    cv.imshow('nameOfWindow4', img)
    cv.imshow('thresholded', thresh)
    
    
    

    
    
cv.waitKey(0)
