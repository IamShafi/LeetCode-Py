# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        ans = self.cur = TreeNode()
        def DFS(r):
            if r:
                DFS(r.left)
                r.left = None
                self.cur.right = r
                self.cur = self.cur.right
                DFS(r.right)
                
        DFS(root)
        return ans.right
        
        