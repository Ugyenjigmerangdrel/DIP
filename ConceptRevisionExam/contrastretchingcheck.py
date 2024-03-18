import numpy as np
import matplotlib.pyplot as plt
import cv2
image = np.array([[6, 7, 5, 5, 6], [6, 5, 6, 7, 4], [7, 5, 6, 6, 6]])

simage = np.array([[1, 2, 1,5,6], [2, 3, 6,7,4], [7,2,2,5,6]])

dx, dy = np.shape(image)
simage = image.copy()

hist = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
for i in range(0, dx):
    for j in range(0, dy):
        simage[i, j] = (image[i, j] - np.min(image)) * (7) / (np.max(image) - np.min(image))
        if hist.get(image[i, j]) is None:
            hist[image[i, j]] = 1
        else:
            hist[image[i, j]] += 1
shist = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
for i in range(0, dx):
    for j in range(0, dy):
        if shist.get(simage[i, j]) is None:
            shist[simage[i, j]] = 1
        else:
            shist[simage[i, j]] += 1
print(hist)
plt.plot(hist.keys(), shist.keys())
plt.bar(hist.keys(), hist.values())
plt.bar(shist.keys(), shist.values())
plt.show()
print(image)