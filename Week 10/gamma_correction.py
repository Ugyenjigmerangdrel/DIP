import cv2
import numpy as np


img = cv2.imread("lena.jpg")


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


gamma = 2.5


lookup_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(256)]).astype(
    np.uint8
)


img_corrected = cv2.LUT(img, lookup_table)


cv2.imshow("Original Image", img)
cv2.imshow("Gamma Corrected Image", img_corrected)

cv2.waitKey(0)
cv2.destroyAllWindows()
