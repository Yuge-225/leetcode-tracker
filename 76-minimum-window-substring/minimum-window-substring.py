class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for char in t:
            need[char] = need.get(char,0) + 1
        
        window = {}
        left,right = 0,0
        valid = 0
        min_len = float("inf")
        start = 0

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] = window.get(c,0) + 1
                
                if window[c] == need[c]:
                    valid += 1
            
            while len(need) == valid:
                if right - left < min_len:
                    start = left
                    min_len = right - left
                
                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if min_len == float("inf") else s[start:start+min_len]

