import numpy as np

def filter2D(image, kernel):
    # Get image dimensions
    height, width = image.shape
    k_height, k_width = kernel.shape

    # Pad the image to handle border pixels
    pad_height = k_height // 2
    pad_width = k_width // 2
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')
    print(padded_image)
    # Initialize the filtered image
    filtered_image = np.zeros_like(image)

    # Apply the filter using convolution
    for i in range(height):
        for j in range(width):
            filtered_image[i, j] = np.sum(padded_image[i:i+k_height, j:j+k_width] * kernel)
        
    return filtered_image

# Example usage
if __name__ == "__main__":
    # Define an image and a kernel
    image = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

    kernel = np.array([[0, 1, 0],
                       [1, -4, 1],
                       [0, 1, 0]])

    # Apply the filter
    filtered_image = filter2D(image, kernel)
    print("Filtered Image:")
    print(filtered_image)
