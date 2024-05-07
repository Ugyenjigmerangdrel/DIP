import cv2
import numpy as np

original_img = cv2.imread("gnoise.png", cv2.IMREAD_GRAYSCALE)

img = np.pad(original_img, 2, mode="symmetric")



# Define the maximum window size (Smax)
Smax = 11
# Function to apply the Adaptive Median Filter
def adaptive_mid_filter(img, Smax):
    output = np.zeros_like(img, dtype=np.uint8)
    padding = Smax // 2

    for i in range(padding, img.shape[0] - padding):
        for j in range(padding, img.shape[1] - padding):
            window_size = 3  # Start with a 3x3 window
            zxy = img[i, j]

            while window_size <= Smax:
                window = img[
                    i - window_size // 2 : i + window_size // 2 + 1,
                    j - window_size // 2 : j + window_size // 2 + 1,
                ].astype(np.uint32)
                zmin = np.min(window)
                zmax = np.max(window)
                zmid = int((zmin + zmax) / 2)

                A1 = zmid - zmin
                A2 = zmid - zmax

                if A1 > 0 and A2 < 0:
                    B1 = zxy - zmin
                    B2 = zxy - zmax

                    if B1 > 0 and B2 < 0:
                        output[i, j] = zxy
                    else:
                        output[i, j] = zmid
                    break
                else:
                    window_size += 2  # Increase the window size for the next iteration

            if window_size > Smax:
                output[i, j] = zmid

    return output

# Apply the Adaptive Median Filter
filtered_img = adaptive_mid_filter(img, Smax)

cv2.imshow("Original Image", original_img)
# cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Adaptive Median Filter Image", filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

