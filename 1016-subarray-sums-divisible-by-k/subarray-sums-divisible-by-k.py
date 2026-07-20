class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
           # ( presum[i] - presum[j] ) % k == 0
        presum = 0
        count = 0 
        remainderTable = {0:1} # remainder:occur time
       
        for num in nums:
            presum += num
            remainder = presum % k

            if remainder in remainderTable:
                count += remainderTable[remainder]
                remainderTable[remainder] += 1
            else:
                remainderTable[remainder] = 1

        return count





"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = [0] * (n+1)
        for i in range(1,n+1):
            preSum[i] = preSum[i-1] + nums[i-1]
        
        count = 0
        remainderTable = {0:1} #key：r, val: number of occurrence for r
        for i in range(1,n+1):
            target = preSum[i] % k
            if target in remainderTable:
                count += remainderTable[target]
                remainderTable[target] += 1
            else:
                remainderTable[target] = 1

        return count



"""