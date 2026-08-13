class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_ele = float("inf")
        for i in range(len(nums)):
            if nums[i] < min_ele:
                min_ele = nums[i]
        return min_ele