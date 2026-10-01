"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import json
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clones = {node: Node(node.val)}
        queue = [node]

        while queue:
            cur = queue.pop(0)

            for n in cur.neighbors:
                if n not in clones:
                    clones[n] = Node(n.val)
                    queue.append(n)
                clones[cur].neighbors.append(clones[n])
        return clones[node]
