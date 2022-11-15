import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('assets/brick.jfif')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
kp = orb.detect(gray)
kp, des = orb.compute(gray, kp)
pts = cv2.KeyPoint_convert(kp)

pts = np.int0(pts)


#corners = cv2.goodFeaturesToTrack(gray, 200, 0.5, 10)
#corners = np.int0(corners)

for pt in pts:
    x, y = pt.ravel()
    cv2.circle(img, (x, y), 2, (255,0,0),-1)

pts = np.int0(pts)
#print(pts)
for i in range(len(pts)):
    for j in range(i+1, len(pts)):
        corner1 = tuple(pts[i])
        corner2 = tuple(pts[j])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)


cv2.imshow('corner', img)
cv2.waitKey(0)
plt.imshow(img), plt.show()