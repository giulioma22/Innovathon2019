import numpy as np
import cv2 as cv
from time import sleep

# cap = cv.VideoCapture("white_line_1.mp4")
# cap = cv.VideoCapture("white_line_2.mp4")
cap = cv.VideoCapture("white_line_3.mp4")
# cap = cv.VideoCapture("white_line_4.mp4")

for i in range(1000):
    ret, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_blue = np.array([0,0,190])
    upper_blue = np.array([255,255,225])
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    edges = cv.Canny(mask,50,150,apertureSize = 3)

    # cv.imshow("Normal", frame)
    cv.imshow("White line", mask)
    # cv.imshow("Frame", edges)
    sleep(0.05)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# frame = cv.imread("/home/mmlab/Downloads/white_line.jpg")
# hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
# lower_blue = np.array([235,235,235])
# upper_blue = np.array([255,255,255])
# mask = cv.inRange(frame, lower_blue, upper_blue)

# cv.imshow("White line", frame)
# cv.imshow("White line", mask)
# cv.waitKey(0)