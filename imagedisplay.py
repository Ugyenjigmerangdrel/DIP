import cv2
import numpy as np
 
matx = np.zeros((200,200)) # numpy array with width =200, height=200

for i in range(0, 200):
    for j in range(0, 200):
        if (i + j) % 8 != 0:
            matx[i, j] = 1  # white

cv2.imshow("Zeros matx", matx) # show numpy array
 
cv2.waitKey(0) # wait for ay key to exit window
cv2.destroyAllWindows() # close all windows