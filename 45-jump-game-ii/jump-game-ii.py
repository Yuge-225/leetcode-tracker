class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        farthest = 0 
        jumps = 0
        coverage = 0
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])

            if i == coverage:
                jumps += 1
                coverage = farthest
        return jumps
