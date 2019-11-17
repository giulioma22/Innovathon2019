import cv2 as cv

winStride = (3,3)   # Best is (4,4)
padding = (16,16)
scale = 1.05
meanShift = 1

bBoxes = []

frame = cv.imread("tunnel.jpg")
hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

for i in range(1):
    (rects,weights) = hog.detectMultiScale(frame,winStride=winStride,padding=padding,scale=scale,useMeanshiftGrouping=meanShift)

    for (x,y,w,h) in rects:
        # Draw and count bounding box only if big enough
        if w > 70 and h > 90:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            x1 = w/2
            y1 = h/2
            cx = x + x1
            cy = y + y1
            bBoxes.append([cx,cy])
            print(len(bBoxes))

    cv.imshow("HOG Image", frame)

    if cv.waitKey(0) & 0xFF == ord("q"):
        break