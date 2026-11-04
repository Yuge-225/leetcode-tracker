class Solution:
    def isPalindrome(self, s: str) -> bool:
        judge_s = ""
        for char in s:
            if char.isalpha():
                judge_s += char.lower()
            elif char.isdigit():
                judge_s += char
            else:
                continue
            
        print(judge_s)
        left, right = 0, len(judge_s) - 1
        while left < right:
            if judge_s[left] != judge_s[right]:
                return False
            left += 1
            right -= 1
        return True