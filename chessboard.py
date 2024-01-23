import numpy as np

chessboard = np.zeros((8, 8), dtype=np.uint8)

for i in range(0, 8):
    for j in range(0, 8):
        if (i + j) % 2 != 0:
            chessboard[i, j] = 1  # white

print(chessboard)