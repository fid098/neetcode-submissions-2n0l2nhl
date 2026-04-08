"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {} #map stores original nodes to cloned nodes

        def dfs(node):  
            if node in oldToNew:
                return oldToNew[node] #if already in the map, return its clone

            copy = Node(node.val)  #or create a new node with the same value
            oldToNew[node] = copy #store it in the map
            #clone all neighbors and add them to the clones neightbor list
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None