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
        iterative dfs: setup a queue with the root in it
        pop the left side of the queue, and if that node's left exists, enter it into the queue 
        if that node's righ exists, enter it into the queue 
        increment the level as it goes, and do this until the q == None and return levels 


        """
        if not root:
            return 0

        levels = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levels += 1

        return levels 