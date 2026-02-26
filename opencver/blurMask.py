import cv2 as cv
import numpy as np

img = cv.imread('photosOpenCvEx/Screenshot_20230120_051143.png')

#There are differenlty methods of blurring
#avg: cv.blur(img, (3,3), cv.BORDER_DEFAULT) avg of surronding pizels of kernel 
#Gaussian: cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT) it attaches weight to surrounding pixels
#Median
#Biliteral: Most effective


#rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), (255,255,255), -1)
#cricle = cv.circle(blank.copy(), (200,200), 200, (255,255,255), -1)

#bitwise and - retruns intersection of both iamges
#ba = cv.bitwise_and(rectangle, cricle)

#bitwise or - retruns union of both iamges
#bitwise xor - retruns non intersecting parts of both iamges
#bitwise not - inverts the binary colour

#Masking
#Focus on certain parts of an iamge


if img is not None:
    blank = np.zeros(img.shape[:2], dtype='uint8')
    maske = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, (255,255,255), -1)
    masked = cv.bitwise_and(img, img, mask=maske) 
    
    #img = cv.bilateralFilter(img, 5, 75, 75) 
    img = cv.resize(img, (int(img.shape[1] * 0.3), int(img.shape[0] * 0.3)), interpolation=cv.INTER_AREA)
    masked = cv.resize(masked, (int(masked.shape[1] * 0.3), int(masked.shape[0] * 0.3)), interpolation=cv.INTER_AREA)
    cv.imshow('nameOfWindow4', img)
    cv.imshow('masked', masked)
    #cv.imshow('rect', rectangle)
    #cv.imshow('circ', cricle)
    #cv.imshow('bitwise and', ba)
    
    

cv.waitKey(0)
