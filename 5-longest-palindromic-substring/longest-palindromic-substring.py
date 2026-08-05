class Solution:
    def longestPalindrome(self, s: str) -> str:
        def Palindrome(s,l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
            
        n = len(s)
        res = ""
        for i in range(n):
            s1 = Palindrome(s,i,i)
            s2 = Palindrome(s,i,i+1)
            if len(res) < len(s1):
                res = s1
            if len(res) < len(s2):
                res = s2

        return res