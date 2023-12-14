# works on directly connected components in directed graph

def create_adj(edges):
    adj = {}
    for u,v in edges:
        if u not in adj:
            adj[u] = []
        
        if v not in adj:
            adj[v] = []

        adj[u].append(v)

    return adj

from collections import deque
def count_strongly_connected(adj,v):
    visited = set()
    store_topo = deque([],len(adj))
    for i in adj:
        if i not in visited:
            toposort(adj,i,visited,store_topo)

    # create transpose graph
    transposed_adj:dict[int,list[int]] = {}
    for i in range(v):
        for j in adj[i]:
            if j not in transposed_adj:
                transposed_adj[j] = []  # reversing the direction of an edge
            transposed_adj[j].append(i)

    print(store_topo)
    # do dfs
    visited.clear()
    count = 0
    for i in transposed_adj:
        if i not in visited:
            dfs(transposed_adj,i,visited) # after every successfull dfs we increment the count
            count +=1

    print(count)

def dfs(tranposed_adj,node,visited):
    visited.add(node)
    for nbr in tranposed_adj[node]:
        if nbr not in visited:
            dfs(tranposed_adj,nbr,visited)

def toposort(adj,node,visited,store_topo:deque[int]):
    visited.add(node)
    for nbr in adj[node]:
        if nbr not in visited:
            toposort(adj,nbr,visited,store_topo)
    
    store_topo.append(node)

edges = [
    [1,2],
    [2,0],
    [0,1],
    [1,3],
    [3,4]
]
adj = create_adj(edges)
print(adj)
count_strongly_connected(adj,5)