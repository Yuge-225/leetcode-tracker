class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def nSumTarget(nums,n,start,target):
            sz = len(nums)
            res = []

            if n < 2 or sz - start < n:
                return res
            
            if n == 2:
                left,right = start,sz-1
                while left < right:
                    s = nums[left] + nums[right]
                    left_val,right_val = nums[left], nums[right]

                    if s < target:
                        while left < right and nums[left] == left_val:
                            left += 1
                    elif s > target:
                        while left < right and nums[right] == right_val:
                            right -= 1
                    else:
                        res.append([left_val,right_val])
                        while left < right and nums[left] == left_val:
                            left += 1
                        while left < right and nums[right] == right_val:
                            right -= 1
            else:
                for i in range(start,sz):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    else:
                        sub_res = nSumTarget(nums,n-1,i+1,target-nums[i])

                        for arr in sub_res:
                            res.append([nums[i]] + arr)

            return res

        nums = sorted(nums)
        ans = nSumTarget(nums,4,0,target)
        return ans
