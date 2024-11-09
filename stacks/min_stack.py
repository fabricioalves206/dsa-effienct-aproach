# problem : determine the min value from a stack with O(1) operation

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, newValue):
        self.stack.append(newValue)
        if not self.min_stack or newValue <= self.min_stack[-1]:
            self.min_stack.append(newValue)

    def pop(self):
        if self.stack:
            if self.min_stack[-1] == self.stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None
