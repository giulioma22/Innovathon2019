import numpy as np
import cv2 as cv
from time import sleep

# cap = cv.VideoCapture("white_line_1.mp4")
# cap = cv.VideoCapture("white_line_2.mp4")
cap = cv.VideoCapture("white_line_3.mp4")

for i in range(1000):
    ret, frame = cap.read()
    # Transform into HSV image
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_white = np.array([0,0,200])
    upper_white = np.array([255,255,235])

    # Check for specific range of white
    mask_white = cv.inRange(hsv, lower_white, upper_white)

    # Detect edges
    edges = cv.Canny(mask_white,50,150,apertureSize = 3)

    # cv.imshow("Normal", frame)
    cv.imshow("White line", mask_white)
    cv.imshow("Frame", edges)
    sleep(0.05)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break