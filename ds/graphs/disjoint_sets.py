def makeSet(parent:list[int],size:list[int],n_nodes:int):
    for i in range(0,n_nodes+1):
        parent.append(i)
        size.append(1)
    

def findParent(parent:list[int],a:int):
    if parent[a] == a:
        return a
    parent[a] = findParent(parent,parent[a]) 
    return parent[a]
    # path compression parent[a'] = parent[a] = parent[b] then we directly set parent[a'] = parent[b]

def add_edge(graph:list[int],u,v,w):
    graph.append([u,v,w])

def weighted_union(parent:list[int],size:list[int],a:int,b:int):
    root_A = findParent(parent,a)
    root_B = findParent(parent,b)
    if None != root_A and None != root_B:
        if size[root_A] < size[root_B]:
            parent[root_A] = root_B
            size[root_B] += size[root_A]

        else:
            parent[root_B] = root_A
            size[root_A] += size[root_B]



def kruskals_algo(graph,n_nodes):
    result_mst = []
    w = 0
    for i in range(n_nodes):
        u = findParent(parent,graph[i][0])
        v = findParent(parent,graph[i][1])
        if u != v:
            w += graph[i][2]
            weighted_union(parent,size,u,v)
            result_mst.append([u,v,w])

    print(result_mst)

parent =[]
size = []
graph:list[int] = []

add_edge(graph,5,4,9)
add_edge(graph,4,3,5)
add_edge(graph,5,1,4)
add_edge(graph,1,4,1)
add_edge(graph,1,2,2)
add_edge(graph,4,2,3)
add_edge(graph,3,2,3)
add_edge(graph,3,6,8)
add_edge(graph,6,2,7)

makeSet(parent,size,len(graph))
graph.sort(key = lambda x : x[2])
kruskals_algo(graph,len(graph))



