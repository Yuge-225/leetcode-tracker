class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        cum = 0
        left,right = 0,0
        while right < len(nums):
            c = nums[right]
            right += 1
            cum += c

            while cum >= target:
                res = min(res,right-left) # 先记录当前合法窗口的长度
                d = nums[left]
                left += 1
                cum -= d
                

        return res if res != float("inf") else 0
