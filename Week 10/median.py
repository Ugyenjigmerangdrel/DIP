import cv2
import numpy as np
import random

def add_noise(img):
    noisy_img = img.copy()  # Create a copy of the original image
    row, col, _ = noisy_img.shape

    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)

        # Pick a random channel
        channel=random.randint(0, 2)

        # Color that pixel to white
        noisy_img[y_coord][x_coord][channel] = 255

    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)

        # Pick a random channel
        channel=random.randint(0, 2)

        # Color that pixel to black
        noisy_img[y_coord][x_coord][channel] = 0

    return noisy_img

def custom_median_filter(image):
    pad_size = 1  # 3x3 kernel -> pad size is 1
    height, width, _ = image.shape
    result = np.zeros_like(image)

    for c in range(3):
        padded_image = np.pad(image[:,:,c], ((pad_size, pad_size), (pad_size, pad_size)), mode='constant', constant_values=0)
        for i in range(pad_size, height + pad_size):
            for j in range(pad_size, width + pad_size):
                neighborhood = padded_image[i-pad_size:i+pad_size+1, j-pad_size:j+pad_size+1]
                result[i-pad_size, j-pad_size, c] = np.median(neighborhood)

    return result

# Reading the color image
input_image = cv2.imread('lena.jpg')

# Adding salt-and-pepper noise to a copy of the original image
noisy_img = add_noise(input_image.copy())

# Applying custom median filter without using inbuilt function
median_filtered_img = custom_median_filter(noisy_img)

# Storing the noisy and filtered images
cv2.imwrite('salt_and_pepper_noisy_lena.jpg', noisy_img)
cv2.imwrite('custom_median_filtered_lena.jpg', median_filtered_img)

# Displaying the original, noisy, and filtered images
cv2.imshow('Original Image', input_image)
cv2.imshow('Noisy Image', noisy_img)
cv2.imshow('Custom Median Filtered Image', median_filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()