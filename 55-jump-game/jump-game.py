class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        farthest_reacheable = 0
        for current_idx in range(n):
            if current_idx > farthest_reacheable:
                return False
            jump_distance = nums[current_idx]
            farthest_reacheable = max(farthest_reacheable,jump_distance+current_idx)
        return True
            