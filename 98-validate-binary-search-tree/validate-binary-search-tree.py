# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def solve(root,min_val,max_val):
            if root is None:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            return solve(root.left,min_val,root.val) and solve(root.right,root.val,max_val)
        
        return solve(root,float("-inf"),float("inf"))
            