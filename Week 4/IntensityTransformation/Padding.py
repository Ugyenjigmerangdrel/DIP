import numpy as np

inputmatrix = np.random.randint(255, size=(10,10))

paddingsize = int(input("Enter the size of padding: "))
dx, dy = np.shape(inputmatrix)
outputdim = ((2*paddingsize)+dx, (2*paddingsize)+dy)

outputmatrix =np.zeros(outputdim)
dix, diy = np.shape(outputmatrix)
print(dix, diy)

for i in range(0, dix-(2*paddingsize)):
    for j in range(0, diy-(2*paddingsize)):
        outputmatrix[i+paddingsize][j+paddingsize] = inputmatrix[i][j]

def neighbour_finder(x, y):
    left = (x, y-1) if x > 0 else 0
    top = (x-1, y) if y > 0 else 0
    leftcorner = (x-1, y-1)
    return [left, top, leftcorner]

for i in range(0+paddingsize, dix-(2*paddingsize)):
    for j in range(0+paddingsize, diy-(2*paddingsize)):
        neighbor = neighbour_finder(i, j)
        print(neighbor)
        lx, ly = neighbor[0]
        tx, ty = neighbor[1]
        tlx, tly = neighbor[2]

        if outputmatrix[lx][ly] == 0:
            outputmatrix[lx][ly] = outputmatrix[i][j]
        elif outputmatrix[tx][ty] == 0:
            outputmatrix[tx][ty] = outputmatrix[i][j]
        elif outputmatrix[tlx][tly] == 0:
            outputmatrix[tlx][tly] = outputmatrix[i][j]




print(outputmatrix)
