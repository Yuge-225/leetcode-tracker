# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def solve(nums):
            if not nums:
                return 
            root_val = max(nums)
            root_idx = -1
            for i in range(len(nums)):
                if nums[i] == root_val:
                    root_idx = i
            root = TreeNode(root_val)
            root.left = solve(nums[:root_idx])
            root.right = solve(nums[root_idx+1:])
            return root

        root = TreeNode(max(nums))
        return solve(nums)




"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def solve(nums):
            if not nums:
                return None
            
            root_idx = nums.index(max(nums))
            root = TreeNode(nums[root_idx])

            root.left = solve(nums[:root_idx])
            root.right = solve(nums[root_idx+1:])
            
            return root
        
        return solve(nums)

            

            
            
            
"""