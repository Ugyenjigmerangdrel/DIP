import cv2
import numpy as np

# Load the noisy input image
original_img = np.array([
    [52, 250, 54, 48, 47, 55, 49],
    [48, 250, 52, 48, 49, 250, 45],
    [250, 55, 250, 250, 51, 250, 48],
    [46, 48, 250, 250, 53, 46, 49],
    [48, 54, 52, 46, 250, 55, 250],
    [46, 250, 52, 250, 250, 250, 50],
    [51, 48, 250, 48, 52, 50, 46]
])

img = np.pad(original_img, 2, mode="symmetric")

# Define the maximum window size (Smax)
Smax = 5

# Function to apply the Adaptive Median Filter
def adaptive_median_filter(img, Smax):
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
                ]
                zmin = np.min(window)
                zmax = np.max(window)
                zmed = np.median(window)

                A1 = zmed - zmin
                A2 = zmed - zmax

                if A1 > 0 and A2 < 0:
                    B1 = zxy - zmin
                    B2 = zxy - zmax

                    if B1 > 0 and B2 < 0:
                        output[i, j] = zxy
                    else:
                        output[i, j] = zmed
                    break
                else:
                    window_size += 2  # Increase the window size for the next iteration

            if window_size > Smax:
                output[i, j] = zmed

    return output


# Apply the Adaptive Median Filter
filtered_img = adaptive_median_filter(img, Smax)

# Display the original and filtered images
print("Original Image")
print(original_img)

dx, dy = np.shape(original_img)
print("Adpative median filter")
print(filtered_img[2:dx+2, 2:dy+2])
