import math


graph = {
    1: [(1,2,7), (1,8,2)],
    2: [(2,1,7), (2,3,4), (2,4,1), (2,6,5)],
    3: [(3,2,4), (3,8,8)],
    4: [(4,2,1), (4,5,6), (4,6,8), (4,7,3), (4,8,3)],
    5: [(5,4,6), (5,8,6), (5,9,8)],
    6: [(6,2,5), (6,4,8)],
    7: [(7,4,3), (7,4,0), (7,5,0)],
    8: [(8,4,0), (8,6,0)],
    9: [],
    10: []
}

graphMat = [
    [0, 7, -1, -1, -1, -1, -1, 2, -1, -1],
    [7, 0, 4, 1, -1, 5, -1, -1, -1, -1],
    [-1, 4, 0, -1, -1, -1, -1, 8, -1, -1],
    [-1, 1, -1, 0, 6, 8, 3, 3, -1, -1],
    [-1, -1, -1, 6, 0, -1, -1, 6, 8, -1],
    [-1, 5, -1, 8, -1, 0, -1, -1, -1, -1],
    [-1, -1, -1, 3, -1, -1, 0, -1, 9, 2],
    [2, -1, 8, 3, 6, -1, -1, 0, -1, -1],
    [-1, -1, -1, -1, 8, -1, 9, -1, 0, -1],
    [-1, -1, -1, -1, -1, -1, 2, -1, -1, 0]
]

visited = [False]*len(graphMat)
T = []
x = y = 0
while False in visited:
    minimum = math.inf
    for i in range(len(visited)):
        if visited[i] == True:
            for j in range(len(graphMat[i])):
                if graphMat[i][j] == 0 or graphMat[i][j] == -1 or visited[j] == True:
                    continue
                elif minimum > graphMat[i][j]:
                    minimum = graphMat[i][j]
                    x = i
                    y = j
    visited[y] = True
    T.append((x + 1, y + 1, minimum))
for i in T:
    print(i)