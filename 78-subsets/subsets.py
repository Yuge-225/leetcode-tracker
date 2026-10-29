class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        track = []

        def backtrack(start):
            res.append(track[:])
            for i in range(start,len(nums)):
                track.append(nums[i])
                backtrack(i+1)
                track.pop()
        backtrack(0)
        return res