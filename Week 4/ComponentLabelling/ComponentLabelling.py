import numpy as np

originalmatrix = np.zeros((10, 10), dtype=np.uint8)
dx, dy = np.shape(originalmatrix)
cx,cy = dx//2, dy//2
#Object one definition
originalmatrix[0:(cx-1), 1:(cy-1)] = 1
originalmatrix[1:(cx-2), (cy-1):(cy+1)] = 1

#Object Two Definition
originalmatrix[(cx+1):(cx+3), 1:(cy-1)] = 1
originalmatrix[(cx+2):(cx+4), (cy-1):(cy+1)] = 1
originalmatrix[(cx+4):(cx+5), 1:(cy)] = 1
print(originalmatrix, "\n")

output_matrix = np.zeros_like(originalmatrix, dtype=np.uint8)
#neighbor finder
def neighbour_finder(x, y):
    left = output_matrix[x - 1][y] if x > 0 else 0
    top = output_matrix[x][y - 1] if y > 0 else 0
    return [left, top]

label = 0
count = 0
pass_count = 1
special_cases = []

for i in range(0, dx):
    for j in range(0, dy):
        if originalmatrix[i][j] == 1:
            if output_matrix[i][j] == 0:
                l, t = neighbour_finder(i, j)
                #case1
                if l == 0 and t == 0:
                    label += 1
                    count += 1
                    output_matrix[i][j] = label
                #case2
                elif l != 0 and t == 0:
                    output_matrix[i][j] = l
                #case3
                elif l == 0 and t != 0:
                    output_matrix[i][j] = t
                #case4
                elif l != 0 and t != 0:
                    #subcase a
                    if l == t:
                        output_matrix[i][j] = l
                    #subcase b
                    elif l != t:
                        count -= 1
                        
                        pass_count += 1
                        for z in range(len(special_cases)):
                            if l in special_cases[z] or t in special_cases[z]:
                                special_cases[z].append(max(l, t))
                        else:
                            special_cases.append([l, t])
                        output_matrix[i][j] = l
                        
print(special_cases)
print("\nAfter Pass 1: \n",output_matrix)

if len(special_cases) > 0 and pass_count == 2:
    for i in range(len(output_matrix)):
        for j in range(len(output_matrix[i])):
            for z in range(len(special_cases)):
                if output_matrix[i][j] != 0 and output_matrix[i][j] in special_cases[z]:
                    output_matrix[i][j] = min(special_cases[z])

print("\nAfter Pass 2: \n",output_matrix)
print("Number of Objects: ", count)


