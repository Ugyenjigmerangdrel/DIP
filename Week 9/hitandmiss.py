import cv2 
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('hm.png', cv2.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
ret,image = cv2.threshold(img,250,255,cv2.THRESH_BINARY)
print(image)
elemestruturante = np.array(([1,1,1],[1,1,1],[1,1,1]), dtype=int)
SaidaHitOrMiss = cv2.morphologyEx(image, cv2.MORPH_HITMISS, elemestruturante)
cv2.imwrite('SaidaHitOrMiss.png', SaidaHitOrMiss)
cv2.imshow('HitOrMiss', SaidaHitOrMiss)
cv2.waitKey(0)