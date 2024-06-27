graph = {
    'A': [('A','B',6), ('A', 'C', 4), ('A', 'D', 5)],
    'B': [('B','E',-1)],
    'C': [('C','B',-2), ('C','E',3)],
    'D': [('D','C',-2), ('D','F',3)],
    'E': [('E','F',3)],
    'F': []
}
costs = {i: float('inf') for i in graph.keys()}
lst = []
for i in graph.values():
    for j in i:
        lst.append((j[0], j[1]))

for i in range(len(graph.keys()) - 1):
    for i in lst:
        for j in graph[i[0]]:
            if j[1] == i[1]:
                if costs[i[1]] > j[2]:
                    costs[i[1]] = j[2]
print(costs)