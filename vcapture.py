import cv2
import numpy as np
from matplotlib import pyplot as plt 

cap = cv2.VideoCapture(0)

#Video Output
fourcc = cv2.VideoWriter_fourcc(*'WMV1')
out = cv2.VideoWriter('Second Capture.wmv', fourcc, 20.00, (640,480))


print("!!!!!!PRESS Q TO QUIT!!!!!!")

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        frame = cv2.flip(frame, 1)
        
        #change color from BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #Set lower and upper boundaries of colour to keep
        lower_blue = np.array([90, 50, 50])
        upper_blue = np.array([130, 255, 255])

        #Create visual representation of wanted pixels
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        #Apply mask to filter out unwanted pixels
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)

        #write the flipped frame
        #out.write(frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

