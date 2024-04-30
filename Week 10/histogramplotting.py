import cv2
import matplotlib.pyplot as plt


img = cv2.imread("lena.jpg")


b, g, r = cv2.split(img)


plt.figure(figsize=(10, 6))


plt.hist(b.ravel(), 256, [0, 256], color="b", label="Blue")
plt.hist(g.ravel(), 256, [0, 256], color="g", label="Green")
plt.hist(r.ravel(), 256, [0, 256], color="r", label="Red")


plt.title("Histogram for Color Scale Picture")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")


plt.legend()


plt.show()
