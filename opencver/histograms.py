import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photosOpenCvEx/Screenshot_20230120_051143.png')

#Histograms - shows distrubution of pixel intensity


    
if img is not None:
    blank = np.zeros(img.shape[:2], dtype='uint8')
    mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 300, (255,255,255), -1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    mask2 = cv.bitwise_and(gray, gray, mask=mask)
     
    #Colour histogram or grayscale histogram
    #Colour one:
    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist = cv.calcHist([img], [i], None, [256], [0,256]) #channels, mask, histSize(bins), ranges
        plt.plot(hist, color=col)
        plt.xlim([0,256])
       
    #Would pass in a list of images, channels, mask, histSize(bins), ranges
    gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
    plt.figure()
    plt.title('Grayscale Histogram Example')
    plt.xlabel("Bins")
    plt.ylabel("Num of Pixels")
    plt.plot(gray_hist)
    plt.xlim([0, 256])
    plt.show()
    
    img = cv.resize(img, (int(img.shape[1] * 0.3), int(img.shape[0] * 0.3)), interpolation=cv.INTER_AREA)
    cv.imshow('nameOfWindow4', img)
    cv.imshow("mask", mask2)
    

    
    
cv.waitKey(0)
