class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = s.split()
        new_s = ""

        for word in words:
            for char in word:
                if char.isalpha() or char.isdigit():
                    new_s += char.lower()
                else:
                    continue
        print(new_s)
        left = 0
        right = len(new_s) - 1
        while left < right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1
        return True








"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = s.split(' ')
        processed_s = []
        for word in words:
            for char in word:
                if char.isalnum():
                    processed_s.append(char.lower())
                else:
                    continue
        left,right = 0, len(processed_s) - 1
        print(processed_s)
        while left <= right:
            if processed_s[left] != processed_s[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True

"""