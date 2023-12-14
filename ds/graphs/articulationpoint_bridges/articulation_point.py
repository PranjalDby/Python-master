from collections import defaultdict


def add_egde(edges):
    adjlist = dict()

    for u,v in edges:
        if u not in adjlist:
            adjlist[u] = []
        
        if v not in adjlist:
            adjlist[v] = []

        adjlist[u].append(v)
        adjlist[v].append(u)

    return adjlist

def articulation_point(adjList,src):
    parent = [-1] * (len(adj)+2)
    visited = set()
    low = [-1] * (len(adj) + 2) # keep track of the lowest minimum time to reach to that node except from parent
    disc = [-1] * (len(adj) + 2)# track of the when for the first time that particular node is visited
    AP = []
    timer = 0
    # print(parent)
    # print(low)
    # print(disc)
    for i in adjList:
        if i not in visited:
            dfs(adjList,i,timer,parent,visited,disc,low,AP)

    
    return AP

def dfs(adjList,node,timer,parent,visited,disc,low,AP):
    visited.add(node)
    timer += 1
    disc[node] = timer
    low[node] = timer
    child = 0
    for nbr in adjList[node]:
        if parent[node] == nbr:
            continue
        if nbr not in visited:
            parent[nbr] = node

            dfs(adjList,nbr,timer,parent,visited,disc,low,AP)
            low[node] = min(low[node],low[nbr])
            if low[nbr] >= disc[node] and parent[node] != -1: # checking if node is {articulation} point or not
                AP.append(node) 

            child += 1
        else:
            low[node] = min(low[node],disc[nbr])
            print(f" disc of  neigh {nbr} = {disc[nbr]}")

    # checking if root node is AP or not it will be AP if it has more than 1 child
    if parent[node] == -1 and child > 1:
        AP.append(node)


edges = [
    [0,1],
    [0,3],
    [4,3],
    [0,4],
    [1,2],
    [8,7],
    [8,9]
    
]

adj = add_egde(edges)
print(adj)
Ap = articulation_point(adj,0)
print(Ap)
