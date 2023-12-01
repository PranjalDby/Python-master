import array
import queue
def create(data):
    adj_list = {}
    for edge in data:
        a,b,w = edge
        if a not in adj_list:
            adj_list[a] = []
        if b not in adj_list:
            adj_list[b] = []
        
        adj_list[a].append([b,w])
        adj_list[b].append([a,w])

    return adj_list;


def dijkstras(graph,start):
    distance = array.array('i',) * len(graph)
    p_qu = queue.PriorityQueue(len(graph))
    p_qu.put((start,0))
    for i in range(0,len(graph)):
        distance.append(1000000)
    distance[start] = 0
    while not p_qu.empty():
        pair = p_qu.get()
        curr_Node = pair[0]
        weight = pair[1]
        for neighbour in graph[curr_Node]:
            to_node = neighbour[0]
            to_weight = neighbour[1]
            if distance[to_node] > distance[curr_Node] + to_weight:
                distance[to_node] = distance[curr_Node] + to_weight
                p_qu.put((to_node,distance[to_node]))
        
    print(distance)

        


data = [
    [0,1,7],
    [0,2,1],
    [0,3,2],
    [1,2,3],
    [1,4,1],
    [1,3,5],
    [4,3,7]]

edges = [
    [0,1,2],
    [0,2,6],
    [1,3,5],
    [2,3,8],
    [3,5,15],
    [3,4,10],
    [5,4,6],
    [4,6,2],
    [5,6,6]
]
adj_list = create(edges)

dijkstras(adj_list,0)