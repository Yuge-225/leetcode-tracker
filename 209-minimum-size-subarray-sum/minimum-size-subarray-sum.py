class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        left,right =0,0
        cum = 0
        while right < len(nums):
            c = nums[right]
            right += 1
            cum += c

            while cum >= target:
                res = min(res,right-left)
                d = nums[left]
                left += 1
                cum = cum - d
        return res if res != float("inf") else 0