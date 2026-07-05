class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1,n+1):
            preSum[i] = preSum[i-1] + nums[i-1]
        counter = 0
        preSumCounter = {} # key 是 前缀和的数值， value是前缀和出现的次数
        for i in range(n+1):
            target = preSum[i] - k
            if target in preSumCounter:
                counter += preSumCounter[target]
            
            if preSum[i] in preSumCounter:
                preSumCounter[preSum[i]] += 1
            else:
                preSumCounter[preSum[i]] = 1
        
        return counter



















"""

 n = len(nums)
        preSum = [0] * (n+1)
        for i in range(1,n+1):
            preSum[i] = preSum[i-1] + nums[i-1]
        
        preSumCount = {} #key表示前缀和的值，value表示前缀和出现的次数
        counter = 0
        for i in range(n + 1):
            target = preSum[i] - k #我要找的前缀和
            if target in preSumCount:
                counter += preSumCount[target]
            
            # 把当前的前缀和存入哈希表中
            if preSum[i] in preSumCount:
                preSumCount[preSum[i]] += 1
            else: 
                preSumCount[preSum[i]] = 1
        return counter

        
"""