class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        fast = slow = 0
        count = 0
        n = len(nums)
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            else:
                count += 1
            fast += 1


        for i in range(count):
            nums[n-1-i] = 0
        
