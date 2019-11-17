import matplotlib.pyplot as pyplot
import cv2 as cv
from time import sleep

from skimage.feature import hog
from skimage import data, exposure

cap = cv.VideoCapture("white_line_3.mp4")
# hog = cv.HOGDescriptor()

for i in range(1000):
    ret, frame = cap.read()
    fd, hog_image = hog(frame, orientations=8, pixels_per_cell=(16,16),
                    cells_per_block=(1,1),visualize=True,multichannel=True)

    hog_image_rescaled = exposure.rescale_intensity(hog_image,in_range=(0,10))

    # cv.imshow("Normal", frame)
    cv.imshow("White line", hog_image_rescaled)
    # cv.imshow("Frame", edges)
    # sleep(0.05)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break