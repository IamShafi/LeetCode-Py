# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(cur, num):
            #see if root is not null
            if not cur:
                return 0
            
            #multiply the number by 10 before adding current value
            num = num*10 + cur.val
            
            #if this is a leaf node? doesn't have left/right child
            #then simply return the number we just compute it
            if not cur.left and not cur.right:
                return num
            
            #if its not a leaf node, 
            #then compute the numbers for the left subtree and the right subtree
            #return the sum of this values
            return dfs(cur.left, num) + dfs(cur.right, num)
        
        #call the dfs function for the node im gonna pass in the root
        #with initial sum equal to zero
        return dfs(root,0)
            