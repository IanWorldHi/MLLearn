import cv2 as cv


#haar cascade takes in a lot of noise - its not that great
#opencv also has its own face recognition thingy

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #interpolation is method for resizing, ie diffs in squashing img

def changeRes(capture, width, height): #Only webcam
    capture.set(3, width) #3 is the width, 4 is the height, ie 10 is brightness
    capture.set(4, height)

#capture = cv.VideoCapture('opencvVideosEx/WIN_20250303_14_19_33_Pro.mp4')
capture = cv.VideoCapture(0) 

while True:
    isTrue, frame = capture.read() #reads in video frame by frame, bool if succesful
    if not isTrue:
        break
    frame_resized = rescaleFrame(frame, scale=0.7)
    frame_resized = cv.cvtColor(frame_resized, cv.COLOR_BGR2GRAY) 
    frame_resized = cv.flip(frame_resized, 1)
    
    haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    #instance of haar cascade classifier
    faces_rect = haar_cascade.detectMultiScale(frame_resized, scaleFactor=1.1, minNeighbors=1)
    #returns as a list of rectangles
    
    for (a, b, c, d) in faces_rect:
        cv.rectangle(frame_resized, (a, b), (a+c, b+d), (0, 255, 0), thickness=2)
        #img, top left corner, bottom right corner, color, thickness
    
    #frame_resized = cv.GaussianBlur(frame_resized, (3,3), cv.BORDER_DEFAULT)
    #frame_resized = cv.Canny(frame_resized, 75, 125) 
    cv.imshow('Video', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'): #means if d is pressed, break - cv.waitKey(20) means wait 20 ms for a key press, & 0xFF is a bitwise operation to get the last 8 bits of the key press
        break
    
    
    

capture.release()
cv.destroyAllWindows()


