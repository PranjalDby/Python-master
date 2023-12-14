# Depth First Traversal -stack


stack = []

def dfs_traversal(graph,start = 'a'):
    stack.append(start)
    while stack:
        node = stack.pop()
        print(node)
        for neighbour in graph[node]:
                stack.append(neighbour)

def recursive_dfs(graph,start = 'a'):
    print(start)
    for neighbour in graph[start]:
        recursive_dfs(graph,neighbour)



graph = {
    'a' : ['c','b'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

# dfs_traversal(graph)
recursive_dfs(graph)