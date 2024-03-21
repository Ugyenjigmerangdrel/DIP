import numpy as np
import cv2
import matplotlib.pyplot as plt

# Original histogram frequency
original_frequency = {
    0: 300,
    1: 70,
    2: 201,
    3: 329,
    4: 656,
    5: 850,
    6: 900,
    7: 790
}

# Target histogram probability
target_probability = {
    0: 0,
    1: 0.05,
    2: 0.15,
    3: 0.15,
    4: 0.1,
    5: 0.15,
    6: 0.2,
    7: 0.2
}

# Step 1: Compute Cumulative Distribution Function (CDF) for both histograms
original_total_pixels = sum(original_frequency.values())
original_cdf = {}
cumulative_prob = 0
for intensity, count in original_frequency.items():
    cumulative_prob += count / original_total_pixels
    original_cdf[intensity] = cumulative_prob

target_cdf = {}
cumulative_prob = 0
for intensity, prob in target_probability.items():
    cumulative_prob += prob
    target_cdf[intensity] = cumulative_prob

# Step 2: Perform Histogram Matching
matched_values = {}
for orig_intensity, orig_cdf_value in original_cdf.items():
    best_match = None
    min_difference = float('inf')
    for target_intensity, target_cdf_value in target_cdf.items():
        difference = abs(orig_cdf_value - target_cdf_value)
        if difference < min_difference:
            min_difference = difference
            best_match = target_intensity
    matched_values[orig_intensity] = best_match

# Display the original and matched histograms
plt.subplot(2, 1, 1)
plt.bar(original_frequency.keys(), original_frequency.values(), color='b')
plt.title('Original Histogram')

plt.subplot(2, 1, 2)
plt.bar(matched_values.keys(), matched_values.values(), color='r')
plt.title('Matched Histogram')

plt.tight_layout()
plt.show()
