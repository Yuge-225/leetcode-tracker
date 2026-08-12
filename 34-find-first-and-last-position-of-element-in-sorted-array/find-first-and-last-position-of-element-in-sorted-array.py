class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """



        def left_bound(nums,target):
            left,right = 0, len(nums)-1
            while left <= right:
                mid = left + (right-left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    right = mid - 1
            if left >= len(nums) or left < 0:
                return -1
            return left if nums[left] == target else -1
        
        def right_bound(nums,target):
            left,right = 0, len(nums)-1
            while left <= right:
                mid = left + (right-left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    left = mid + 1
            if right >= len(nums) or right < 0:
                return -1
            return right if nums[right] == target else -1
        
        
        
        l = left_bound(nums,target)
        r = right_bound(nums,target)
        return [l,r]