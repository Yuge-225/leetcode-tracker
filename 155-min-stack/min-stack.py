class MinStack:

    def __init__(self):
        self.stack = []
        self.help_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.help_stack) == 0:
            self.help_stack.append(value)
        else:
            self.help_stack.append(min(value,self.help_stack[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.help_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.help_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.help_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.help_stack:
            self.help_stack.append(min(value,self.help_stack[-1]))
        else:
            self.help_stack.append(value)
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.help_stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.stack:
            return self.help_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
"""