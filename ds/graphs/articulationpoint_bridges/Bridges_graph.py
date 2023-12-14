def create_adj(edges):
    adj_list = {}

    for a,b in edges:
        if a not in adj_list:
            adj_list[a] = []

        if b not in adj_list:
            adj_list[b] = []

        adj_list[a].append(b)
        adj_list[b].append(a)

    return adj_list


def make_set(parent,disc,low,n):
    for i in range(n+1):
        parent.append(-1)
        disc.append(-1)
        low.append(-1)


def find_bridges(graph,src):
    # Using DFS
    visited.add(src)
    result = []
    timer = 0
    for neigh in graph[src]:
        if neigh not in visited:
            visited.add(neigh)
            # calling for dfs
            print(f"calling dfs for node = {neigh}")
            dfs(graph,neigh,parent,timer,disc,low,result,visited)

    return result

def dfs(graph,node,parent,timer,disc,low,result,visited):
    visited.add(node)
    timer = timer + 1
    disc[node] = timer # keep track of the node which we reached first
    low[node] = timer  # keep track of the lowest possible time by which we can reach to that node other than parent
    for nbr in graph[node]:
        if parent[node] == nbr:
            print(f'parent = {node}')
            continue
        if nbr not in visited:
            parent[nbr] = node
            visited.add(nbr)
            dfs(graph,nbr,parent,timer,disc,low,result,visited)
            low[node] = min(low[node],low[nbr])
            # check edge is bridge
            if low[nbr] > disc[node]:
                result.append((nbr,node))
        else:
            #updating the low of node with minimum
            # its a backedge
            low[node] = min(low[node],disc[nbr])

    

edges = [[2,1],
         [1,0],
         [2,0],
         [0,4],
         [4,5],
         [4,3],
         [3,5]]

parent = []
visited = set()
disc = []
low = []


adj = create_adj(edges)
print(adj)
make_set(parent,disc,low,len(adj))
print(find_bridges(adj,2))