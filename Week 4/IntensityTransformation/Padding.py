import numpy as np
import cv2

def padding_symmetric(matrix, padding):
    height, width = np.shape(matrix)

    new_height = height + 2 * padding
    new_width = width + 2 * padding

    result_matrix = np.zeros((new_height, new_width), dtype=matrix.dtype)


    result_matrix[padding:padding + height, padding:padding + width] = matrix
    print(result_matrix)
    
    # Reflect horizontally
    for x in range(padding):
        result_matrix[:, x] = result_matrix[:, 2 * padding - x - 1]
        result_matrix[:, new_width - x - 1] = result_matrix[:, new_width - 2 * padding + x]
    print(result_matrix) 
        

    # Reflect vertically
    for y in range(padding):
        result_matrix[y, :] = result_matrix[2 * padding - y - 1, :]
        result_matrix[new_height - y - 1, :] = result_matrix[new_height - 2 * padding + y, :]

    return result_matrix

#image = cv2.imread("bone.png",0)
image = np.random.randint(low=0, high=255, size=(10, 10))
dx, dy = np.shape(image)
padding_width = int(input("Enter pad width: "))

# matrix = np.random.randint(low=0, high=255, size=(x, y))
# print("Original matrix:")
# print(matrix)

result = padding_symmetric(image, padding_width)
print("\nResult matrix:")
print(result)
#cv2.imwrite("padding_symmetric_image.jpg",result)