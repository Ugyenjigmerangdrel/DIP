import numpy as np

image = np.array([
    [52, 250, 54, 48, 47, 55, 49],
    [48, 250, 52, 48, 49, 250, 45],
    [250, 55, 250, 250, 51, 250, 48],
    [46, 48, 250, 250, 53, 46, 49],
    [48, 54, 52, 46, 250, 55, 250],
    [46, 250, 52, 250, 250, 250, 50],
    [51, 48, 250, 48, 52, 50, 46]
])

dx, dy = np.shape(image)

output_image = image.copy()
output_image_1 = image.copy()
output_image_2 = image.copy()
for x in range(1, dx-1):
    for y in range(1, dy-1):
        neighborhood = []
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                neighborhood.append(image[i, j])
        mean = int(np.sum(neighborhood)/len(neighborhood))
        output_image_2[x, y] = mean
        output_image[x, y] = np.min(neighborhood)
        if(image[x, y] == 250):
               output_image_1[x, y] = np.min(neighborhood)
        else:
           output_image_1[x, y] = image[x,y]  

print(image)
print(output_image)
print(output_image_1)
print(output_image_2)
