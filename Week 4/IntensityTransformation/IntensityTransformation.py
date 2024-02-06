import numpy as np
import cv2

img_input = cv2.imread('mamogram.png', 0)
img_output = 255 - img_input

cv2.imshow('input', img_input)
cv2.imshow('negative', img_output)
key = cv2.waitKey(0)

if key==27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('./output/negative.png', img_output)
    cv2.destroyAllWindows()
