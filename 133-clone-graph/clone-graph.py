"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        q = deque([node])
        new = Node(node.val)
        nodes = {node: new}
        while len(q):
            node = q.popleft()
            node_copy = nodes[node]
            for neighbor in node.neighbors:
                if neighbor not in nodes:
                    nodes[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                node_copy.neighbors.append(nodes[neighbor])
        return new