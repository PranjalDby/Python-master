edges = [['i','j'],['k','i'],['m','k'],['k','l'],['o','n']]

def create_adjacency_list(edges):
    graph = {}
    for edge in edges:
        a,b = edge
        if a in graph.keys():
            graph[b] = [a]
            graph[a].append(b)

        elif b in graph.keys():
            graph[a] = [b]
            graph[b].append(a)
        else:
            graph[a] = [b]
            graph[b] = [a]

    return graph

visited = set()
def dfs_traversal(graph,start,dest):
    if start == dest:
        return True
    for neighbour in graph[start]:
        if neighbour not in visited:
            visited.add(neighbour)
            if dfs_traversal(graph,neighbour,dest):
                return True
            
    return False

graph = create_adjacency_list(edges)

num_graph = {
    0:[8,1,5],
    4:[3,2],
    3:[2,4],
    8:[0,5],
    5:[0,8],
    1:[0],
    2:[3,4]
}

