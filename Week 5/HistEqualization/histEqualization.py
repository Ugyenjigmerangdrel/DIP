import numpy as np
import cv2
import matplotlib.pyplot as plt


def histogram_equalization(image):
   # Convert to grayscale if needed
   if len(image.shape) == 3:
       image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   # Calculate the histogram
   hist, bins = np.histogram(image.flatten(), 256, [0, 256])

   # Calculate the cumulative distribution function (CDF)
   cdf = hist.cumsum()

   # Normalize the CDF to [0, 255]
   cdf_m = np.ma.masked_equal(cdf, 0)
   cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
   cdf = np.ma.filled(cdf_m, 0).astype('uint8')

   # Apply the CDF as a lookup table to the image
   image_equalized = cdf[image]

   return image_equalized

# Load the image
inputImage = cv2.imread('beans.png')
hist = cv2.calcHist([inputImage], [0], None, [256], [0, 256])
# Perform histogram equalization
outputImage = histogram_equalization(inputImage)
hist2 = cv2.calcHist([outputImage], [0], None, [256], [0, 256])


# plot the histogram
plt.figure()
plt.title("Input Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

# plot the histogram
plt.figure()
plt.title("Output Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist2)
plt.xlim([0, 256])
plt.show()

# Display or save the equalized image
cv2.imshow('Original Image', inputImage)
cv2.imshow('Equalized Image', outputImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
