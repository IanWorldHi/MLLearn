#(https://www.youtube.com/watch?v=oXlwWbU8l2o) for this they also do "pip install caer" which is a libray they built on top of opencv for easy of us, doubt ill need to use it tho

import cv2 as cv

img = cv.imread('photosOpenCvEx/Screenshot_20230120_050930.png')
#Read an image in as a matrix of pixels

#display image
#if img is not None:
    #cv.imshow('nameOfWindow', img)
    #cv.waitKey(0)
#waits amount of time for a keyboard input, 0 means indefinitely, ie 1000 = 1 sec then quit

capture = cv.VideoCapture('opencvVideosEx/WIN_20250303_14_19_33_Pro.mp4')
#capture = cv.VideoCapture(0) #for webcam, other nums for other cams

while True:
    isTrue, frame = capture.read() #reads in video frame by frame, bool if succesful
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


