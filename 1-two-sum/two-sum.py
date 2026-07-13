class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,x in enumerate(nums):
            complement = target - x
            if complement in seen:
                return [i, seen[complement]]
            else:
                seen[x] = i
        return []