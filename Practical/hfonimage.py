import numpy as np
import matplotlib.pyplot as plt 
import cv2

image=cv2.imread('hole.png', cv2.IMREAD_GRAYSCALE)

window=np.ones((45,45),np.uint8)

def dilate(i, j, image, mask):
    result_img = np.zeros_like(image)
    for x in range(i, image.shape[0]-i):
        for y in range(j, image.shape[1]-j):
            x1 = x - i
            x2 = x + i + 1
            y1 = y - j
            y2 = y + j + 1
            
            roi = image[x1:x2, y1:y2]
            if roi.shape == mask.shape:
                result = np.logical_and(roi, mask)
            else:
                result = mask
                   
            if np.any(result):
                result_img[x, y] = 1
    return result_img
def compliment(image):
    return 1-image

def hole_filling(image, window, start_x, start_y, end_x, end_y):
   
    output_image = np.zeros_like(image)
    output_image[start_x, start_y] = 1

    roi = image[start_x:end_x+1, start_y:end_y+1]

    dilated_roi = dilate(start_x,start_y,roi, window)
    
    output_image[start_x:end_x+1, start_y:end_y+1] = dilated_roi
    inverse=compliment(image)
    output_image=np.logical_and(output_image,inverse)
    
    
    return output_image
            

dx, dy = image.shape
output=hole_filling(image, window,0,0,dx,dy)
filled=output+image
plt.subplot(3,2,1)
plt.imshow(image,cmap='gray')
plt.subplot(3,2,2)
plt.imshow(output,cmap='gray')
plt.subplot(3,2,3)
plt.imshow(compliment(image),cmap='gray')
plt.subplot(3,2,4)
plt.imshow(filled,cmap='gray')
plt.show()