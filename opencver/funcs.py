import cv2 as cv
import numpy as np

img = cv.imread('photosOpenCvEx/Screenshot_20230120_050930.png')
if img is not None:
    #Greyscale - important for just looking at intensity of pixels
    gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    #Blur - removing noise ie edge detection
    blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
    #increasing kernel size increases blur
    
    #edge cascade - dtecting edges
    can= cv.Canny(gray, 75, 125) #lower/upper gradient thresholds, higher = less edges
    
    #dilate image - increase size of edges, can be used to make them more visible or to connect broken edges
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))
    dilated = cv.dilate(can, kernel, iterations=2) #kernel size, iterations is how many times to apply dilation
    
    #erode image, opposite of dilation to reverse it
    
    #cropping cuz img is just array
    cropped = img[200:500, 200:500]
    
    #translation by x, y pixels
    def translate(img, x, y):
        transMat = np.array([[1, 0, x], [0, 1, y]], dtype=np.float32)
        dimensions = (img.shape[1]+150, img.shape[0]+150) #how big the canvas will be
        return cv.warpAffine(img, transMat, dimensions)
    translated = translate(img, 100, 100)
    
    
    cv.imshow('nameOfWindow', translated)
    cv.waitKey(0)


