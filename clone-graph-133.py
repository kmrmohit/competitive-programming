'''
Day 3
1 attempt
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    visited = {}
    def clone(self, old):
        if old is None:
            return None
        newNode = Node(old.val)
        self.visited[old.val] = newNode
        newNeighbors = []
        for node in old.neighbors:
            if self.visited.get(node.val):
                newNeighbors.append(self.visited[node.val])
            else:
                newNeighbors.append(self.clone(node))
        newNode.neighbors = newNeighbors
        return newNode
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.visited = {}
        return self.clone(node)
        