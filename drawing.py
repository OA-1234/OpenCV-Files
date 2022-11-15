import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = np.zeros((512,512,3), np.uint8)

cv2.line(img, (0,0), (512,512),(255,0,0), 5)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.circle(img,(447,63), 63, (0,0,255), -1)

cv2.ellipse(img,(256,256),(100,50),0,-180,180,255,-1)


cv2.imshow('Drawing', img)
cv2.waitKey(0)
cv2.destroyAllWindows()