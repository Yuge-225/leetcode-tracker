import random
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:] 
        self.new = self.original.copy() # 复制一份，而非直接引用

    def reset(self) -> List[int]:
        self.new = self.original.copy() # 复制一份，而非直接引用
        return self.new
        

    def shuffle(self) -> List[int]:
        n = len(self.original)
        for i in range(n-1,-1,-1):
            j = random.randint(0,i)
            self.new[i],self.new[j] = self.new[j],self.new[i]
        return self.new
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()