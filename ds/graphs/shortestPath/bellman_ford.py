
def bellmanford(no_nodes,n_edges,src,dest,edges):
    # creating des

    dist = [float('inf') for i in range(no_nodes + 1)]
    dist[src] = 0 # weight of src is 0

    for i in range(0,no_nodes+1):
        # traverse on edgelist
        for j in range(0,n_edges):
            u = edges[j][0] # src node
            v = edges[j][1] # dest node
            w = edges[j][2] # weight on edges
            if dist[u] != float('inf') and (dist[u] + w) < dist[v]:
                dist[v] = dist[u] + w
            
    # check -ve cycle is present or not
    flag = 0
    for i in range(0,no_nodes+1):
        # traverse on edgelist
        for j in range(0,n_edges):
            u = edges[j][0] # src node
            v = edges[j][1] # dest node
            w = edges[j][2] # weight on edges
            if dist[u] != float('inf') and (dist[u] + w) < dist[v]:
                flag = 1

    if flag == 0:
        return dist[dest]
    
    return -1

edges = [
    [1,2,2],
    [2,3,-1],
    [1,3,2],
]

dis = bellmanford(3,3,1,3,edges)
print(dis)