import cv2
import numpy as np


img = cv2.imread("lena.jpg")


hsi_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


hue_channel = hsi_img[:, :, 0]
saturation_channel = hsi_img[:, :, 1]
intensity_channel = hsi_img[:, :, 2]


lower_intensity = 150
upper_intensity = 250


sliced_intensity = np.zeros_like(intensity_channel)
sliced_intensity[
    (intensity_channel >= lower_intensity) & (intensity_channel <= upper_intensity)
] = 255


merged_hsi_img = cv2.merge([hue_channel, saturation_channel, sliced_intensity])


merged_rgb_img = cv2.cvtColor(merged_hsi_img, cv2.COLOR_HSV2BGR)


cv2.imshow("Original RGB Image", img)
cv2.imshow("HSI Image", hsi_img)
cv2.imshow("Merged Image", merged_rgb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
