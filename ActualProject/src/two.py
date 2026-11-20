from ultralytics import YOLO
import cv2 as cv

model = YOLO("../models/yolo26n-pose.pt")

#constants keypoints
NOSE = 0
L_SHOULDER = 5
R_SHOULDER = 6

#kinda useless now
def rescaleFrame(frame, scale=1.00):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #

def changeRes(capture, width, height): #Only webcam
    capture.set(3, width) #3 is the width, 4 is the height, ie 10 is brightness
    capture.set(4, height)

def onePerson(r):
    if len(r.boxes) == 0:
        return None
    b = r.boxes.xyxy
    areas = (b[:, 2]-b[:, 0])*(b[:, 3]-b[:, 1])
    i = areas.argmax()
    return r.keypoints.data[i].cpu().numpy()

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read() #reads in video frame by frame, bool if succesful
    if not isTrue:
        break
    frame_resized = rescaleFrame(frame, scale=0.7)
    frame_resized = cv.flip(frame_resized, 1)

    r = model(frame_resized, verbose=False)[0] #model inference
    annotated = r.plot()

    cv.imshow('Video', annotated)
    kp = onePerson(r)

    if cv.waitKey(1) & 0xFF==ord('d'): #means if d is pressed, break - cv.waitKey(20) means wait 20 ms for a key press, & 0xFF is a bitwise operation to get the last 8 bits of the key press
        break
    #print(r.boxes.conf, r.keypoints.data)
    print(KeyboardInterrupt)


capture.release()
cv.destroyAllWindows()




























