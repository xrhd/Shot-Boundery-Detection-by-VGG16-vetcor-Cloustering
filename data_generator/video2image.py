import cv2
import numpy as np
import os
import math

videoFile = "./videoplayback.mp4"
imagesFolder = "./data"
# Playing video from file:
try:
    if not os.path.exists(imagesFolder):
        os.makedirs(imagesFolder)
except OSError:
    print ('Error: Creating directory of data')


cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) // 2 #frame rate
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename = imagesFolder + "/image_" +  str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, frame)
cap.release()
print("Done!")