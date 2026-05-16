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
        nodes = {}
        def dfs(node):
            if not node:
                return
            clone_node = Node(node.val)
            nodes[node] = clone_node
            neighbors = []
            for neighbor in node.neighbors:
                if neighbor in nodes:
                    neighbors.append(nodes[neighbor])
                else:
                    neighbors.append(dfs(neighbor))
            clone_node.neighbors = neighbors
            return clone_node
        return dfs(node)