class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        presum = 0
        remainderTable = {0:-1} # r:idx
        for i,num in enumerate(nums):
            presum += num
            remainder = presum % k
            if remainder in remainderTable:
                if i - remainderTable[remainder] >= 2:
                    return True
                else:
                    continue
            else:
                remainderTable[remainder] = i
        return False











"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1,n+1):
            preSum[i] = preSum[i-1] + nums[i-1]

        remainderTable = {0:0} # key是remainder值，val是remainder值首次出现的位置
        for i in range(n+1):
            remainder = preSum[i] % k
            if remainder in remainderTable:
                if i - remainderTable[remainder] >=2:
                    return True
                else:
                    continue
            else:
                remainderTable[remainder] = i
        
        return False

            

"""