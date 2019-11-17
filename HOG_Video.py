import matplotlib.pyplot as pyplot
import cv2 as cv
from time import sleep

winStride = (4,4)
padding = (16,16)
scale = 1.05
meanShift = 1

cap = cv.VideoCapture("white_line_3.mp4")
hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

for i in range(1000):
    
    ret, frame = cap.read()
    (rects,weights) = hog.detectMultiScale(frame,winStride=winStride,padding=padding,scale=scale,useMeanshiftGrouping=meanShift)

    for (x,y,w,h) in rects:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv.imshow("HOG Video", frame)
    # sleep(0.05)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
