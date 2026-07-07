# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         n = len(code)
#         res = [0] * n 
#         if k == 0:
#             return res
#         for i in range(0,n):
#             if k > 0:
#                 for j in range(1,k+1):
#                     element_idx = (i + j) % n
#                     element_val = code[element_idx]
#                     res[i] += element_val
#             else:
#                 for j in range(1,abs(k)+1):
#                     element_idx = (i - j) % n
#                     element_val = code[element_idx]
#                     res[i] += element_val
#         return res



class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        
        if k > 0:
            for i in range(n):
                count = k
                while count > 0:
                    actual_idx = (i + count) % n
                    res[i] += code[actual_idx]
                    count -= 1
        
        if k < 0:
            for i in range(n):
                count = -k
                while count > 0:
                    actual_idx = (i - count) % n
                    res[i] += code[actual_idx]
                    count -= 1
        return res

                    