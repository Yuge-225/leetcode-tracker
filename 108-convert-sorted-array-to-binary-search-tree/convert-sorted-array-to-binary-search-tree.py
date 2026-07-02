# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n <= 0:
            return 
        
        root_idx = n // 2
        print(f"n = {n}, root_idx = {root_idx}, nums[root_idx] = {nums[root_idx]}")
        root = TreeNode(nums[root_idx])
        
        root.left = self.sortedArrayToBST(nums[:root_idx])
        root.right = self.sortedArrayToBST(nums[root_idx+1:])
        return root
