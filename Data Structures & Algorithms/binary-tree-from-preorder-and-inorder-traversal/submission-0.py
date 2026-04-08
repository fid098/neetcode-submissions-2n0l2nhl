# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        #the first element of preorder is always the root
        root = TreeNode(preorder[0])

        #the root of the inorder would be the "mid"
        mid = inorder.index(preorder[0])
        #find the index in inorder where preorder starts 

        #build the left subtree using preorder[1: mid+1] and inorder[0:mid]
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        #build the right subtree using preorder[mid+1:] and inorder[mid+1:]
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        

        return root
