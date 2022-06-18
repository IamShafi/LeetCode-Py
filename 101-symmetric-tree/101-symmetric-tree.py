# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def DFS(leftNode, rightNode):
            #len
            if(not leftNode and rightNode) or (leftNode and not rightNode):
                return False
            if (not leftNode and not rightNode):
                return True
            #val
            if leftNode.val != rightNode.val:
                return False
            
            return DFS(leftNode.left, rightNode.right) and DFS(leftNode.right, rightNode.left)
            
        return DFS(root.left, root.right)
        