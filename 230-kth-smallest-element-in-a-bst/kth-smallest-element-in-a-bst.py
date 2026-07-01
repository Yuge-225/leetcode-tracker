# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_ord = []
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            in_ord.append(root.val)
            traverse(root.right)
        traverse(root)
        return  in_ord[k-1]
