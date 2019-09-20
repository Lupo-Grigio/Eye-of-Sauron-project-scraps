# USAGE

# import the necessary packages
import imutils
from imutils.video import VideoStream
import numpy as np
import time
import cv2
import sys

Default_confidence = 0.5
EyeCenterX = 800 # eye X and Y are 0 to 1600 0 up left 1600 down right
EyeCenterY = 800

# load our serialized model from disk
# net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")

# initialize the video stream and allow the cammera sensor to warmup
vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:
    # grab the frame from the threaded video stream and resize it
    # to have a maximum width of 400 pixels
    frameflipped = vs.read()
    # for tracking the image needs to be flipped
    frame = cv2.flip(frameflipped,1)
    frame = imutils.resize(frame, width=400)
 
    # grab the frame dimensions and convert it to a blob
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
        (300, 300), (104.0, 177.0, 123.0))
 
    # pass the blob through the network and obtain the detections and
    # predictions
    net.setInput(blob)
    detections = net.forward()

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence

        if confidence < Default_confidence:
            continue

        # compute the (x, y)-coordinates of the bounding box for the
        # object
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
 
        # draw the bounding box of the face along with the associated
        # probability
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY),
            (0, 0, 255), 2)
        Xcenter = float((startX + endX) / 2)
        Ycenter = float((startY + endY) / 2)
        # TODO: I have the center of the rectangle, now I need the center of the frame
        # so I can calculate an offset, that I can use against the scale of the output
        # what I need is the arduino map function...
        # w and h are the width and height of the frame, from earlier
        # so w/2 and h/2 is the center of the frame...
        # startX,endX is my source range, 0 and w is my dest range
        # XCenter is what percentage of W? 
        XCenterPerc = float(Xcenter / w)
        YCenterPerc = float(Ycenter / h)
        rangedX = XCenterPerc * 1600
        rangedY = YCenterPerc * 1600
        sys.stdout.write( str(int(rangedX)) + ',' + str(int(rangedY)) + '\n' )
        sys.stdout.flush()
        cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
 
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()