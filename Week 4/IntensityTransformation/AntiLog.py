import cv2
import math
import numpy as np

img_input = cv2.imread('mri.png', 0)
img_input2 = cv2.imread('map.png', 0)



dx, dy = np.shape(img_input)
#y less than 1
img_output = np.array(1 * np.power(img_input/255, 0.3))
#y greater than one
img_output2 = np.array(1 * np.power(img_input2/255, 3))

cv2.imshow('input', img_input)
cv2.imshow('gamma', img_output)
#cv2.imshow('input', img_input2)
#cv2.imshow('gamma', img_output2)
key = cv2.waitKey(0)

if key==27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('./output/log.png', img_output)
    cv2.destroyAllWindows()
