import numpy as np
import cv2
import matplotlib.pyplot as plt

# Given histogram frequency
frequency = {
    0: 300,
    1: 70,
    2: 201,
    3: 329,
    4: 656,
    5: 850,
    6: 900,
    7: 790
}

# Step 1: Compute Probability Distribution
total_pixels = sum(frequency.values())
probability = {}
for intensity, count in frequency.items():
    probability[intensity] = count / total_pixels

# Step 2: Compute Cumulative Distribution Function (CDF)
cdf = {}
cumulative_prob = 0
for intensity, prob in probability.items():
    cumulative_prob += prob
    cdf[intensity] = cumulative_prob

# Step 3: Equalize the Histogram
equalized_value = {}
for intensity, cdf_value in cdf.items():
    equalized_value[intensity] = round(cdf_value * 7)

# Display the original and equalized histograms
plt.subplot(2, 1, 1)
plt.bar(frequency.keys(), frequency.values(), color='b')
plt.title('Original Histogram')

plt.subplot(2, 1, 2)
plt.bar(equalized_value.keys(), equalized_value.values(), color='r')
plt.title('Equalized Histogram')

plt.tight_layout()
plt.show()

