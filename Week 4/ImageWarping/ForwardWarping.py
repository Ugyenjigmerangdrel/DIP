import numpy as np
import math

# Define input image
input_image = np.zeros((10, 10))
dx, dy = np.shape(input_image)
cx = dx//2
cy = dy//2
input_image[((cx)-5):((cx)-3), ((cy)-5):((cy)-1)] = 1

# Declare forward transfer function
func = int(input("Enter 1 for rotation: "))
if func == 1:
    a = np.pi/2

def forward_transfer_function(x, y):
    if func == 1:
        tmatrix = np.array([[np.cos(a), np.sin(a), 0], [-np.sin(a), np.cos(a), 0], [0, 0, 1]])
        imatrix = np.array([[x],[y],[1]])
        transformed_mat = np.matmul(tmatrix, imatrix)
        xi, yi = transformed_mat[0][0], transformed_mat[1][0]
        return xi, yi
    #return xi, yi

# Initialize output image
output_image = np.zeros_like(input_image)


# Map the four corners from input to output while applying forward transfer function
corners = [(0, 0), (0, dy-1), (dx-1, 0), (dx-1, dy-1)]

#print(corners)
for corner in corners:
    x, y = corner
    new_x, new_y = forward_transfer_function(x, y)
    
    output_image[math.ceil(new_x), math.ceil(new_y)] = input_image[x, y]
    #print(math.ceil(new_x), math.ceil(new_y))


# Apply forward transfer function on all coordinates of input image
transformed_raw_coordinates = []
for x in range(dx):
    for y in range(dy):
        new_x, new_y = forward_transfer_function(x, y)
        if 0 <= new_x < output_image.shape[0] and 0 <= new_y < output_image.shape[1]:
            transformed_raw_coordinates.append((new_x, new_y))

print(transformed_raw_coordinates)

print("Input Matrix\n",input_image)
# Print the output image
print(output_image)
