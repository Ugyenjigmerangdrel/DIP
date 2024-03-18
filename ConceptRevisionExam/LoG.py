import numpy as np

def gaussian_filter(image, n, sigma):
  """
  Creates a Gaussian filter kernel and applies convolution to the image.

  Args:
      image: A 2D NumPy array representing the grayscale image.
      n: Size of the filter kernel (n x n).
      sigma: Standard deviation of the Gaussian function.

  Returns:
      A 2D NumPy array representing the filtered image.
  """

  # Calculate filter weights
  x, y = np.ogrid[-n//2:n//2+1, -n//2:n//2+1]
  kernel = np.exp(-(x**2 + y**2) / (2.0 * sigma**2)) / (2.0 * np.pi * sigma**2)
  kernel /= np.sum(kernel)  # Normalize weights

  # Apply convolution using NumPy's built-in function
  filtered_image = np.convolve(image, kernel, mode='same')

  return filtered_image

# Example usage
image = np.array([[100, 120, 150],  # Sample image data
                   [80, 180, 200],
                   [50, 100, 130]])

n = 3  # Filter size (3x3)
sigma = 1  # Standard deviation

filtered_image = gaussian_filter(image, n, sigma)

print(filtered_image)
