# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        recursive dfs: 1 + the max of the maxdepth of both leaves 
        iterative bfs: setup a queue with the root in it
        pop the left side of the queue, and if that node's left exists, enter it into the queue 
        if that node's righ exists, enter it into the queue 
        increment the level as it goes, and do this until the q == None and return levels 
        iterative dfs: setup a stack with the root and its depth, while there is something in the stack,
        we pop the node, depth, if the node is not null, we append its left and right nodes and their depths + 1
        keep a res that increments the depth as it goes 

        """
        stack = [[root, 1]]

        res = 0

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

        