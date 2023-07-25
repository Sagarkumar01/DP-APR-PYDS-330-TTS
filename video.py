import cv2
import numpy as np

cap = cv2.VideoCapture('C:\Users\91902\Documents\my course\XlO9.gif')

#if the camera is not open
if(cap.isOpened()==False):
    print("Error opening video stream or file")

# Read the entire file untill it is comlected
while(cap.isOpened()):
    #capture frame by frame
    ret, frame = cap.read()
    if ret == True:
     # display the resulting frame
        cv2.imshow('Frame',frame)
      #press Q on keyboard to exit
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        #
        else:
            break


        cap.release()



        cv.destroyAllwindow()


