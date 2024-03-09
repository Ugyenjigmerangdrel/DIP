import numpy as np
import cv2

#adaptive median filter applications

image = cv2.imread('sandpnoisy.png', cv2.IMREAD_GRAYSCALE)
image = cv2.copyMakeBorder(image, 3, 3, 3, 3, cv2.BORDER_CONSTANT)
dx, dy = np.shape(image)
output = np.zeros_like(image, dtype=np.float32)
smax = (7, 7)

def stageA(sxy):
    zmin = np.min(sxy)
    zmax = np.max(sxy)
    zmed = np.median(sxy)
    a1 = zmed - zmin
    a2 = zmed - zmax
    return zmin, zmax, zmed, a1, a2

def stageB(sxy, zmin, zmax):
    b1 = sxy[i, j] - zmin
    b2 = sxy[i, j] - zmax
    return b1, b2

for i in range(dx):
    for j in range(dy):
        sxy = np.min
        print(np.min(sxy))
        # zmin, zmax, zmed, a1, a2 = stageA(sxy)
        # if a1 > 0 and a2 < 0:
        #     b1, b2 = stageB(sxy, zmin, zmax)
        #     if b1 > 0 and b2<0:
        #         output[i, j] = sxy[i, j]
        #     else:
        #         output[i, j] = zmed
        # else:
        #     sxy = image[i-2:i+3, j-2:j+3]
        #     if np.shape(sxy) <= smax:
        #         zmin, zmax, zmed, a1, a2 = stageA(sxy)
        #         if a1 > 0 and a2 < 0:
        #             b1, b2 = stageB(sxy, zmin, zmax)
        #             if b1 > 0 and b2<0:
        #                 output[i, j] = sxy[i, j]
        #         else:
        #             output[i, j] = zmed
        #     else:
        #        output[i, j] = zmed

 





print(dx, dy)

cv2.imshow('Noise', image)
cv2.imshow('Final', output)
cv2.waitKey(0)