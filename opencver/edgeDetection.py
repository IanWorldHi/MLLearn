import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('photosOpenCvEx/Screenshot_20230120_051143.png')



if img is not None:
    blank = np.zeros(img.shape[:2], dtype='uint8')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    #Laplocian method: computes gradients then grabs edges (high change in gradient)
    lap = cv.Laplacian(gray, cv.CV_64F)
    #img, data depth
    lap = np.absolute(lap).astype(np.uint8)
    
    #Sobel method: computes gradients in x and y direction then adds them together to get edges
    sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
    sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
    #img, data depth, x order, y order
    combined = cv.bitwise_or(sobelx, sobely)
    
    #Canny: one stage of canny is actually sobel
    canny = cv.Canny(gray, 150, 175)
    
    
    img = cv.resize(img, (int(img.shape[1] * 0.3), int(img.shape[0] * 0.3)), interpolation=cv.INTER_AREA)
    lap = cv.resize(lap, (int(lap.shape[1] * 0.3), int(lap.shape[0] * 0.3)), interpolation=cv.INTER_AREA)
    combined = cv.resize(combined, (int(combined.shape[1] * 0.3), int(combined.shape[0] * 0.3)), interpolation=cv.INTER_AREA)
    canny = cv.resize(canny, (int(canny.shape[1] * 0.3), int(canny.shape[0] * 0.3)), interpolation=cv.INTER_AREA)
    
    cv.imshow('nameOfWindow4', img)
    cv.imshow('laplacian', lap)
    cv.imshow('sobel', combined)
    cv.imshow('canny', canny)
    
    

    
    
cv.waitKey(0)
