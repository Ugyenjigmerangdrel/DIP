import cv2
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

image_path = 'bone.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


def histogram_plot(image):
    intensity_counts = {}
    dx, dy = np.shape(image)
    for i in range(dx):
        for j in range(dy):
            if image[i][j] in intensity_counts:
                intensity_counts[image[i][j]] += 1
            else:
                intensity_counts[image[i][j]] = 1

    intensity_values = []
    intensity_frequencies = []

    for value in range(256):
        intensity_values.append(value)
        intensity_frequencies.append(intensity_counts.get(value, 0))

    # Create a Seaborn histogram
    print(intensity_counts)
    print(intensity_values)
    print(intensity_frequencies)

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=intensity_values, y=intensity_frequencies, palette="rocket")
    plt.title("Histogram of Pixel Intensities")
    plt.xlabel("Intensity")
    plt.ylabel("Frequency")
    plt.xticks(np.arange(0, 256, 10))
    plt.show()

histogram_plot(image)