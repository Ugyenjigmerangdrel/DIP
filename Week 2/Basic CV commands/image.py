import numpy as np

#we refer to image as matrix
image = np.array([[0,1,0,0], [0,0,0,0], [0,0,0,0]])
#image dimension readingg
dx, dy = np.shape(image)

#image traversing/ reading the image and editing image
for i in range(dx):
    for j in range(dy):
        image[i][j] = 1


print(image)