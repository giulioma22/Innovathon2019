import numpy as np
import cv2 as cv

def hog_compute(im):
    hist = hog.compute(im,winStride,padding,locations)
    samples.append(hist)
    return np.float32(samples)

cap = cv.VideoCapture("white_line_3.mp4")

samples = []
winSize = (64,64)
blockSize = (16,16)
blockStride = (8,8)
cellSize = (8,8)
nbins = 9
derivAperture = 1
winSigma = 4.
histogramNormType = 0
L2HysThreshold = 2.0000000000000001e-01
gammaCorrection = 0
nlevels = 64
hog = cv.HOGDescriptor(winSize,blockSize,blockStride,cellSize,
                    nbins,derivAperture,winSigma,histogramNormType,
                    L2HysThreshold,gammaCorrection,nlevels)
winStride = (8,8)
padding = (8,8)
locations = ((10,20),(30,30),(50,50),(70,70),(90,90),(110,110),
            (130,130),(150,150),(170,170),(190,190))

for i in range(1000):
    ret, frame = cap.read()
    new_hog = hog_compute(frame)
    cv.imshow("White line", new_hog)
    # cv.imshow("Frame", edges)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
