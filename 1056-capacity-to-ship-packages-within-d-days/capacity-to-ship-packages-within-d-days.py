class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        def days_required(weights,k):
            day = 1
            capacity_oneday = 0
            for i in range(len(weights)):
                if capacity_oneday + weights[i] > k:
                    day += 1
                    capacity_oneday = 0
                    capacity_oneday += weights[i]
                else:
                    capacity_oneday += weights[i]
            return day

        while left < right:
            mid = left + (right-left) // 2
            if days_required(weights,mid) > days:
                left = mid + 1
            else:
                right = mid
        
        return left
