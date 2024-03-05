import numpy as np

#matrix = np.matrix('0, 1, 1; 0, 1, 0; 0, 0, 1')

matrix = np.matrix('0, 1, 1; 0, 1, 0; 0, 0, 1')

def fourConnected(xp, yp, xq, yq):
    n4p = []
    n4p.append((xp-1,yp))
    n4p.append((xp+1,yp))
    n4p.append((xp,yp-1))
    n4p.append((xp, yp+1))
    #print(n4p)

    if matrix[xp, yp] == matrix[xq, yq]:
        if (xq, yq) in n4p:
            return "They are 4-Connected"
        else:
            return "They are not 4-Connected"
    else:
        return "They are not 4-Connected"

def eightConnected(xp, yp, xq, yq):
    n8p = []
    n8p.append((xp-1,yp))
    n8p.append((xp+1,yp))
    n8p.append((xp,yp-1))
    n8p.append((xp, yp+1))
    n8p.append((xp-1,yp-1))
    n8p.append((xp+1,yp-1))
    n8p.append((xp-1,yp+1))
    n8p.append((xp+1, yp+1))

    if matrix[xp, yp] == matrix[xq, yq]:
        if (xq, yq) in n8p:
            return "They are 8-Connected"
        else:
            return "They are not 8-Connected"
    else:
        return "They are not 8-Connected"

def mixConnected(xp, yp, xq, yq):
    n4p = []
    ndp = []
    n4q = []
    n4p.append((xp-1,yp)) #top
    n4p.append((xp+1,yp)) #bottom
    n4p.append((xp,yp-1)) #left
    n4p.append((xp, yp+1)) #right
    ndp.append((xp-1,yp-1))
    ndp.append((xp+1,yp-1))
    ndp.append((xp-1,yp+1))
    ndp.append((xp+1, yp+1))
    n4q.append((xq-1,yq))
    n4q.append((xq+1,yq))
    n4q.append((xq,yq-1))
    n4q.append((xq, yq+1))

    """
    Theory
    c) m-adjacency(mixed adjacency): Two pixels p and q with values from V are m-adjacent if and only if
        1) q is in N4(p), or
        2) q is in ND(p) and the set N4(p)∩N4(q) has no pixels whose values are from V.
    """
    #print(ndp)
    if matrix[xp, yp] == matrix[xq, yq]:
        if (xq, yq) in n4p:
            return "They are M-Connected"
        elif (xq, yq) in ndp:
            insec = []
            for i in n4p:
                for j in n4q:
                    if i == j:
                        insec.append(i)
            print(insec)
            if len(insec) > 0:
                for k in insec:
                    
                    if matrix[xq, yq] == 1 and matrix[k[0], k[1]] == 1: #condition checks if the the intersectiion of N4p and N4q has pixels of V basically her V = {1}
                        return "They are not M-Connected"
                    else:
                        return "They are M-Connected"
                return "They are M-Connected"
            else:
                return "They are not M-Connected"
        else:
            return "They are not M-Connected"
    else:
        return "They are not M-Connected"


print(matrix)
xp = int(input("Xp:"))
yp = int(input("Yp:"))
xq = int(input("Xq:"))
yq = int(input("Yq:"))
#print(fourConnected(xp, yp, xq, yq))
print(mixConnected(xp, yp, xq, yq))

# p -> 1,1(1)
# v = [1]
# q -> 0,2(1)
# n4p -> 0,1; 1,0; 1,2; 2,1; no
# ndp -> 0,0; 2,0; 0,2; 2,2; yes
# N4(p)∩N4(q) has no pixels whose values are from V.
# n4q -> 0, 1; 1, 2;
# N4(p)∩N4(q) -> 0,1(1); 1,2(0); conditions not m connected




