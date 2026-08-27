class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        best = 0
        while left < right:
            min_height = min(height[left],height[right])
            curr = (right-left) * min_height
            best = max(curr,best)
            # 我们只移动最短柱子，因为每次移动，宽度都减少，如果要找到更大面积，不能移动最长柱子
            if min_height == height[left]:
                left += 1
            else:
                right -= 1
        return best

"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0
        while left < right:
            curr_area = min(height[left],height[right]) * (right-left)
            max_area = max(max_area,curr_area)

            if min(height[left],height[right]) == height[left]:
                left += 1
            else:
                right -= 1
                
        return max_area



"""