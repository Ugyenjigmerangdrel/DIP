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

# Define function to compute harmonic mean filter
def harmonic_mean_filter(image, kernel_size):
    # Pad the image to handle border pixels
    padded_img = np.pad(image, ((1, 1), (1, 1)), mode='constant')
    filtered_img = np.zeros_like(image)
    
    # Apply harmonic mean filter
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            window = padded_img[i:i+kernel_size, j:j+kernel_size]
            non_zero_vals = window[window != 0]
            if len(non_zero_vals) == 0:
                filtered_img[i, j] = 0
            else:
                filtered_img[i, j] = len(non_zero_vals) / np.sum(1.0 / non_zero_vals)
    
    return filtered_img

# Apply the harmonic mean filter to the image
filtered_img = harmonic_mean_filter(original_img, kernel_size=3)

# Clip the resulting values to ensure they remain within the valid range for image data
filtered_img = np.clip(filtered_img, 0, 255)

print("Original Image:")
print(original_img)
print("\nFiltered Image:")
print(filtered_img)
