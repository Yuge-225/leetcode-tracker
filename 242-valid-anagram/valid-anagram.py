class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        for x in s:
            s_count[x] = s_count.get(x,0) + 1
        t_count = {}
        for x in t:
            t_count[x] = t_count.get(x,0) + 1
        
        return t_count == s_count
        
        









"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        for char in t:
            count_t[char] = count_t.get(char,0) + 1
        return count_s == count_t
        
        
"""