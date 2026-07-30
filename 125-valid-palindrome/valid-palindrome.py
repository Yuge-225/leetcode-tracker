class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = s.split(' ')
        processed_s = []
        for word in words:
            for char in word:
                if ord(char.lower()) >= ord('a') and ord(char.lower()) <= ord('z'):
                    processed_s.append(char.lower())
                elif char.isdigit():
                    processed_s.append(char)
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
