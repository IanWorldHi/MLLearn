import cv2 as cv
import numpy as np

img = cv.imread('photosOpenCvEx/Screenshot_20230120_051143.png')

#There are differenlty methods of blurring
#avg: cv.blur(img, (3,3), cv.BORDER_DEFAULT) avg of surronding pizels of kernel 
#Gaussian: cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT) it attaches weight to surrounding pixels
#Median
#Biliteral: Most effective

blank = np.zeros((400, 400, 3), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), (255,255,255), -1)
cricle = cv.circle(blank.copy(), (200,200), 200, (255,255,255), -1)

#bitwise and
ba = cv.bitwise_and(rectangle, cricle)


if img is not None:
    #img = cv.bilateralFilter(img, 5, 75, 75) 
    #cv.imshow('nameOfWindow4', img)
    cv.imshow('rect', rectangle)
    cv.imshow('circ', cricle)
    cv.imshow('bitwise and', ba)
    

cv.waitKey(0)
