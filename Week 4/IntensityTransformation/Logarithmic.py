import cv2
import math
import numpy as np

img_input = cv2.imread('star.png', 0)
dx, dy = np.shape(img_input)
img_output = np.zeros((dx,dy))

L = 256

c = ((L-1)/np.log2(1 + np.max(img_input)))

for i in range(dx):
    for j in range(dy):
        img_output[i][j] = c*math.log2(1 + img_input[i][j])

cv2.imshow('input', img_input)
cv2.imshow('log', img_output)
key = cv2.waitKey(0)

if key==27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('./output/log.png', img_output)
    cv2.destroyAllWindows()
