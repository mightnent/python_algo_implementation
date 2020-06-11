from collections import deque

def bfs(graph,node):
    #using the deque functions creates a doubly linked list
    Q = deque([node])
    level = {node:0}
    parent = {node:None}
    while Q:
        n = Q.popleft()
        for i in graph[n]:
            if n not in level:
                Q.append(n)
                level[i] = level[n] +1
                parent[i] = n
    return level,parent

