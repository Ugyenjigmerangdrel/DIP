import numpy as np

def bilinear_interpolation(matrix, new_shape):
    # Get the dimensions of the original matrix
    height, width = matrix.shape

    # Calculate the scaling factors
    scale_height = height / new_shape[0]
    scale_width = width / new_shape[1]

    # Generate the indices for the new matrix
    new_indices = np.indices(new_shape)

    # Scale the indices
    scaled_indices = new_indices * np.array([[scale_height], [scale_width]])

    # Calculate the integer and fractional parts of the indices
    int_indices = scaled_indices.astype(int)
    frac_indices = scaled_indices - int_indices

    # Perform bilinear interpolation
    interpolated_matrix = (1 - frac_indices[0]) * (1 - frac_indices[1]) * matrix[int_indices[0], int_indices[1]] + \
                          frac_indices[0] * (1 - frac_indices[1]) * matrix[int_indices[0] + 1, int_indices[1]] + \
                          (1 - frac_indices[0]) * frac_indices[1] * matrix[int_indices[0], int_indices[1] + 1] + \
                          frac_indices[0] * frac_indices[1] * matrix[int_indices[0] + 1, int_indices[1] + 1]

    return interpolated_matrix

matrix = np.random.randint(0, 10, (5, 5))
imatrix = bilinear_interpolation(matrix, (10, 10))
print(imatrix)