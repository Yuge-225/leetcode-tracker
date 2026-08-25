class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_need(k):
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / k) 
            return hour
        
        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right-left) // 2
            if hours_need(mid) > h:
                left = mid + 1
            elif hours_need(mid) <= h:
                right = mid
        return left