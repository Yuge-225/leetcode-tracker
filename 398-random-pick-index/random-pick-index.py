import random
from collections import defaultdict
class Solution:
    def __init__(self, nums):
        self.dict = defaultdict(list)
        for i,x in enumerate(nums):            
            self.dict[x].append(i)

    def pick(self, target):
        candidate_indices = self.dict[target]
        return random.choice(candidate_indices)
