class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        boundary = {}
        for i,char in enumerate(s):
            boundary[char] = i
        far_bound = 0
        start = 0
        res = []
        for i,char in enumerate(s):
            far_bound = max(far_bound,boundary[char])

            if i == far_bound:
                res.append(far_bound+1 - start)
                start = i+1
                
        return res

