class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        slow = fast = 0
        shown = set()
        while fast  < len(nums):
            if nums[fast] not in shown:
                shown.add(nums[fast])
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow