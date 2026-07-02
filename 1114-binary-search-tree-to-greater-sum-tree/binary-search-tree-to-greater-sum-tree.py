# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0 
        def traverse(root):
            if root is None:
                return
            traverse(root.right)
            self.sum += root.val
            root.val  = self.sum
            traverse(root.left)
        
        traverse(root)
        return root
