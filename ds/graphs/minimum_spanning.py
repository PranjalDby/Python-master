from collections import defaultdict
import queue
import heapq
def create_adj(edges):
    graph = {}
    for edge in edges:
        a, b, w = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append((b, w))
        graph[b].append((a, w))

    return graph


em = enumerate([-1, -1, -1, -1, -1])


def MST(adj, src):
    parent = {i: v for i, v in em}
    mst = defaultdict(set)
    visited = set([src])
    edges = [
        (src,neigh,w) for neigh,w in adj[src]
    ]
    print("Edges = ",edges)
    heapq.heapify(edges)
    while edges:
        u, v, w = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst[u].add((v, w))
            parent[v] = u
            for neigh, w in adj[v]:
                if neigh not in visited:
                    heapq.heappush(edges, (v, neigh, w))

    print(parent)
    return mst



lists = [
    [0, 1, 2],
    [0, 3, 6],
    [1, 2, 3],
    [1, 4, 5],
    [2, 4, 7],
    [3, 1, 8]]
adj_list = create_adj(lists)
# print(adj_list)
print(MST(adj_list, 0))
