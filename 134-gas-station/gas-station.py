class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        curr_tank = 0
        ttl_tank  = 0
        start_point = 0
        for i in range(n):
            diff = gas[i] - cost[i]
            curr_tank += diff
            ttl_tank += diff
            if curr_tank < 0:
                start_point = i+1
                curr_tank = 0
        
        if ttl_tank >= 0:
            return start_point
        else:
            return -1
        