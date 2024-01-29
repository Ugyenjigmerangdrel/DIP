import numpy as np

def nearest_neighbor_interpolation(image, scale_factor):
    # Get the dimensions of the original image
    height, width = image.shape

    # Calculate the dimensions of the scaled image
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)

    # Create an empty matrix for the scaled image
    scaled_image = np.zeros((new_height, new_width), dtype=np.uint8)

    # Iterate over each pixel in the scaled image
    for i in range(new_height):
        for j in range(new_width):
            # Calculate the corresponding pixel position in the original image
            original_i = int(i / scale_factor)
            original_j = int(j / scale_factor)

            # Assign the nearest neighbor pixel value to the scaled image
            scaled_image[i, j] = image[original_i, original_j]

    return scaled_image

# Example usage
image = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

scale_factor = 1.5
scaled_image = nearest_neighbor_interpolation(image, scale_factor)

print("Original Image:")
print(image)

print("\nScaled Image:")
print(scaled_image)
