import matplotlib.pyplot as pyplot
import cv2 as cv
from time import sleep

winStride = (3,3)   # Best is (4,4)
padding = (16,16)
scale = 1.05
meanShift = 1

frame = cv.imread("tunnel.jpg")
hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

for i in range(1):
    
    (rects,weights) = hog.detectMultiScale(frame,winStride=winStride,padding=padding,scale=scale,useMeanshiftGrouping=meanShift)
    
    for (x,y,w,h) in rects:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv.imshow("HOG Image", frame)

    if cv.waitKey(0) & 0xFF == ord("q"):
        break