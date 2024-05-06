import numpy as np
import cv2

input_image = cv2.imread('compre.jpg', cv2.IMREAD_GRAYSCALE)

#defining filter mask and size
filter_gaussian = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]], dtype=int)

filter_gaussian2 = np.array([
    [1,1,1,1,1],
    [1,2,2,2,1],
    [1,2,4,2,1],
    [1,2,2,2,1],
    [1,1,1,1,1]], dtype=int)

print(np.sum(filter_gaussian2  ))

filter_gaussian3 = np.array([
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,2,2,2,1,1],
    [1,1,2,4,2,1,1],
    [1,1,2,2,2,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1]], dtype=int)

factor = 1/36
padding_factor = 2
#function definition
def smoothImage(input_image, padding_factor, filter, factor):
    padded_image = cv2.copyMakeBorder(input_image, padding_factor, padding_factor, padding_factor, padding_factor, cv2.BORDER_CONSTANT)
    output_image = np.zeros_like(input_image, dtype=np.uint8)

    for i in range(padding_factor, input_image.shape[0] + padding_factor):
        for j in range(padding_factor, input_image.shape[1] + padding_factor):
                output_image[i-padding_factor, j-padding_factor] = int(np.sum(padded_image[i-padding_factor:i+padding_factor + 1, j-padding_factor:j+padding_factor+1] * filter) * factor)
    return output_image, padded_image


output_image, padded_image = smoothImage(input_image, padding_factor, filter_gaussian2, factor)

final_image = input_image - output_image

final_output = input_image + (factor*final_image)

cv2.imshow('Original Image', input_image)
cv2.imshow('Smoothed Image', output_image)
cv2.imshow('Final Image', final_image)
cv2.imshow('Final Output', final_output)
cv2.waitKey(0)