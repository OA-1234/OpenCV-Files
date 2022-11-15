import cv2
import numpy as np
from matplotlib import pyplot as plt


#img = cv2.imread(r"assets\check.jpg", 1)
img = plt.imread("assets/check.jpg")
print(img)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 10, 0.0001, 9)
corners = np.int0(corners)


for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255,0,0), -1)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)


#cv2.imshow('Corners', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
plt.imshow(img), plt.show()