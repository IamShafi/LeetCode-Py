# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def DFS(node):
            if not node:
                return
            if node.val == target.val:
                return node
            return DFS(node.left) or DFS(node.right)  
        return DFS(cloned)