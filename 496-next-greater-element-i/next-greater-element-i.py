class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        mid_dict = {}
        stack = []

        for i in range(n):
            while stack and nums2[i] > nums2[stack[-1]]:
                top = stack.pop()
                key = nums2[top]
                val = nums2[i]
                mid_dict[key] = val
            stack.append(i)
        
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in mid_dict:
                res[i] = mid_dict[nums1[i]]
            else:
                continue
        return res        











"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stack = []
        mid_dict = {}

        for i in range(n):
            while stack and nums2[i] > nums2[stack[-1]]:
                top = stack.pop()
                key = nums2[top]
                value = nums2[i]
                mid_dict[key] = value

            stack.append(i)
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in mid_dict:
                res[i] = mid_dict[nums1[i]]
            else:
                continue
        return res
        
        

"""