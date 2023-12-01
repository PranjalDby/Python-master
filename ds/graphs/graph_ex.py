from collections import deque
graph2 = {
    'f':['g','i'],
    'g':['h'],
    'h':[],
    'i':['g','k'],
    'j':['i'],
    'k':[],
}

# Has Path
is_visited = []
def has_path(graph,source,destination):
    stack = [source]      
    while len(stack) > 0:
        curr = stack.pop()
        if curr == destination:
            return True
        for neighbour in graph[curr]:
            stack.append(neighbour)
    
    return False

def has_path_recur(graph,source,des):
    if source == des:
        return True
    
    for neighbour in graph[source]:
        if has_path_recur(graph,neighbour,des):
            return True
        
    return False

# count connected components
def count_connected_components(graph,count=0):
    visited = set()
    for node in graph.keys():
        if explore(graph,node,visited):
            count += 1

    return count

def explore(graph,node,visited):
    if node in visited:
        return False
    
    visited.add(node)
    for neighbour in graph[node]:
        explore(graph,neighbour,visited)

    return True

# largest Component
max_count = []
def count_helper(graph,node,visited,count):
    if node in visited:
        return count-1
    
    visited.add(node)
    for neighbour in graph[node]:
        count+=1
        count_helper(graph,neighbour,visited,count)

    return count
def largest_component(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            max_count.append(count_helper(graph,node,visited,1))
    
    if max_count is not None:
        max_count.sort()
        return max_count[-1]


# Shortest Path

visited  = set()
q = deque()
def shortest_path(graph,start,dest,distance= 0):
   
    while len(q) > 0:
        curr,distance= q.popleft()
        print(curr)
        if curr == dest:
            return distance
        
        for neighbours in graph[curr]:
            if neighbours not in visited:
                q.append([neighbours,distance+1])
                visited.add(neighbours)
                
    return -1
    
def create_adjacency_list(edges):
    graph = {}
    for edge in edges:
        a,b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
        
            
    return graph


edges = [['w','x'],['x','y'],['z','y'],['z','v'],['w','v']]

graph = create_adjacency_list(edges)
print(graph)
# print(shortest_path(graph,'w','z'))

# Islands Count

land_matrix  = [
    [0,1,0,0,1,1],
    [1,1,0,0,1,0],
    [0,1,0,0,0,0],
    [0,0,0,1,1,0],
    [0,1,0,1,1,0],
    [0,0,0,0,0,0]
]

matrix = [[1,0,2,3],[0,0,0,0],[4,0,5,6],[7,0,0,8],[9,10,0,11]]

visited = set()
def island_count(land_matrix):
    count = 0
    for i in range(0,len(land_matrix)):
        for j in range(0,len(land_matrix[0][:])):
            if explore_island(land_matrix,i,j,visited):
                count += 1
    
    return count
        
def explore_island(grid,r,c,visited):
    rowinbounds = 0 < r and r < len(grid)
    colinbounds = 0 < c and c < len(grid[0][:])
    if not rowinbounds or not colinbounds:
        return False
    
    if grid[r][c] == 0:
        return False
    
    pos = (r,c)
    if pos in visited:
        return False
    
    visited.add(pos)
    
    explore_island(grid,r-1,c,visited) # up
    explore_island(grid,r+1,c,visited) # down
    explore_island(grid,r,c-1,visited) # left
    explore_island(grid,r,c+1,visited) # right
    
    return True


def minimum_count(matrix):
    count = 1
    min = 100000000
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0][:])):
                count = explore_island_count(matrix,i,j,visited)
                if count < min and count > 0:
                    min = count
                
                
                
                    
        
    return min
        
def explore_island_count(matrix,r,c,visited):
    count = 1
    rowinbounds = 0 <= r and r < len(matrix)
    colinbounds = 0 <= c and c < len(matrix[0][:])
    
    if not rowinbounds or not colinbounds:
        return 0
    
    if matrix[r][c] == 0:
        return 0
    
    pos = (r,c)
    if pos in visited:
        return 0
    
    visited.add(pos)
    count = 1
    count += explore_island_count(matrix,r-1,c,visited) # up
    count += explore_island_count(matrix,r+1,c,visited) # down
    count += explore_island_count(matrix,r,c-1,visited) # left
    count += explore_island_count(matrix,r,c+1,visited) # right
    
    return count


print(minimum_count(matrix))
            
                