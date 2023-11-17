# Breadth First Search Implements Queue Data Structure

# always use iterative approach for BFS
from collections import deque
def bfs_traversal(graph,source = 'a'):
    queue = deque(source)
    while len(queue) > 0:
        curr = queue.popleft()
        print(curr)
        for neighbour in graph[curr]:
            queue.append(neighbour)


graph = {
    'a' : ['c','b'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

graph2 = {
    'f':['g','i'],
    'g':['h'],
    'h':[],
    'i':['g','k'],
    'j':['i'],
    'k':[],
}

bfs_traversal(graph)