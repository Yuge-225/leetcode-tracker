# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solve(L_root, R_root):
            if L_root is None and R_root is None:
                return True
            if (L_root and R_root is None) or (L_root is None and R_root):
                return False

            if L_root.val != R_root.val:
                return False
            return solve(L_root.left,R_root.right) and solve(L_root.right,R_root.left)

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