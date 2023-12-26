class Node:
    def __init__(self,val = 0,neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self) -> str:
        return f'{self.val}:{self.neighbors}'

from typing import Optional
from queue import Queue
class Solutions:
    def clone(self,node:Node| None):
        clone = dict()
        q = Queue()
        clone[node] = Node(node.val)
        q.put(node)
        while not q.empty():
            curr = q.get()
            print(curr.val)
            for nbrs in curr.neighbors:
                if nbrs not in clone:
                    clone[nbrs] = Node(nbrs.val)
                    q.put(nbrs)

                clone[curr].neighbors.append(clone[nbrs])

        print(clone[node])


node = Node(1,[Node(2),Node(4)])
# print(node.neighbors)
node.neighbors[0].neighbors.append(Node(3))
node.neighbors[1].neighbors.append(Node(node.val,node.neighbors))
node.neighbors[0].neighbors[0].neighbors.append(Node(node.neighbors[1].val,node.neighbors[1].neighbors))
sol = Solutions()
sol.clone(node)
# nbr of four