class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')','[':']','{':'}'}
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if stack and char == pairs[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0