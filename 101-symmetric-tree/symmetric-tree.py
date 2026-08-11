# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def solve(left,right):
            if not left and not right:
                return True
            if not left and right or left and not right:
                return False
            if left.val != right.val:
                return False

            return solve(left.left,right.right) and solve(left.right,right.left)
        
        return solve(root.left, root.right)
            










"""
def solve(left_tree,right_tree):
            if (left_tree is None and right_tree is None):
                return True
            elif (left_tree is None and right_tree) or (left_tree and right_tree is None):
                return False
            elif left_tree.val != right_tree.val:
                return False
            else:
                return solve(left_tree.left,right_tree.right) and solve(left_tree.right,right_tree.left)

        return solve(root.left,root.right)
        


"""