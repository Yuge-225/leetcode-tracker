class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        net_gas = 0
        curr_tank = 0
        start_pt = 0
        for i in range(n):
            diff = gas[i] - cost[i]
            curr_tank += diff
            net_gas += diff
            if curr_tank < 0:
                start_pt = i + 1
                curr_tank = 0
        return start_pt if net_gas >= 0 else -1
