import numpy as np

def dilation(image, kernel):
    output = np.zeros_like(image)
    image_padded = np.pad(image, ((1,1),(1,1)), mode='constant', constant_values=0)
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            if np.all(image_padded[y:y+3, x:x+3] == kernel):
                output[y, x] = 1
    return output

def erosion(image, kernel):
    output = np.zeros_like(image)
    image_padded = np.pad(image, ((1,1),(1,1)), mode='constant', constant_values=1)
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            if np.all(image_padded[y:y+3, x:x+3] == kernel):
                output[y, x] = 1
    return output

def hit_or_miss(image, J_kernel, K_kernel):
    J_complement = np.logical_not(J_kernel)
    K_complement = np.logical_not(K_kernel)
    
    erosion_J = erosion(image, J_kernel)
    erosion_K_complement = erosion(image, K_complement)
    
    return np.logical_and(erosion_J, erosion_K_complement)

# Example usage:
image = np.array([[0, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0],
                  [0, 1, 1, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0]])

J_kernel = np.array([[0, 1, 0],
                     [1, 1, 1],
                     [0, 1, 0]])

K_kernel = np.array([[1, 0, 1],
                     [0, 0, 0],
                     [1, 0, 1]])

result = hit_or_miss(image, J_kernel, K_kernel)
print("Result:")
print(result)
