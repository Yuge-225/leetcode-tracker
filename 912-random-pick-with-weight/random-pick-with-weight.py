class Solution:
    def __init__(self, w: List[int]):
        total = 0
        self.presum = []
        for weight in w:
            total += weight
            self.presum.append(total)
        self.total = total
        
    def pickIndex(self) -> int:
        target = random.randint(1,self.total)
        left = 0
        right = len(self.presum) - 1
        while left < right:
            mid = left + (right-left) // 2
            if target > self.presum[mid]:
                left = mid + 1
            else:
                right = mid
        return left



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()