# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: #if subroot doesnt exist 
            return True
        if not root:  #if root doesnt exist 
            return False

        if self.sameTree(root, subRoot):  #call the sameTree function on the node
            return True

        #if not the start of the subroot, compare the left or right with recursion 
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        #if root or subroot doesnt exist
        if not root and not subRoot:
            return True
        
        #if root and subroot exists and they are equal value 
        if root and subRoot and root.val == subRoot.val:
            #call main function on left and right for root and subroot 
            return (self.sameTree(root.left, subRoot.left) and
            self.sameTree(root.right, subRoot.right))
        return False
