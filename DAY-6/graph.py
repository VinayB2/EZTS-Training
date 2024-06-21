graph = {
    1: [(1,2,0), (1,3,0)],
    2: [(2,1,0), (2,7,0)],
    3: [(3,1,0), (3,5,0), (3,6,0)],
    4: [(4,7,0), (4,8,0)],
    5: [(5,3,0), (5,7,0)],
    6: [(6,3,0), (6,8,0)],
    7: [(7,2,0), (7,4,0), (7,5,0)],
    8: [(8,4,0), (8,6,0)]
}


def DFS(graph):
    visited = {}
    for i in graph.keys():
        visited[i] = False
    stack = []
    DFShelper(graph, visited, stack, 1)

def DFShelper(graph, v, s, e):
    if v[e] == False:
        s.append(e)
        v[e] = True
    else:
        return
    for i in graph[e]:
        DFShelper(graph, v, s, i[1])
    print(s.pop())
def BFS(G):
    BFShelper(G, 1)
def BFShelper(G, e):
    Q = [e]
    v= {}
    for i in G.keys():
        v[i] = False
    v[e] = True
    while len(Q) != 0:
        curr = Q.pop(0)
        print(curr,end=' ')
        for i in G[curr]:
            if v[i[1]] == False:
                Q.append(i[1])
                v[i[1]] = True
BFS(graph)
            