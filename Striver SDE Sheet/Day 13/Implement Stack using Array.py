#Question Link: https://takeuforward.org/data-structure/implement-stack-using-array/


class Solution:
    def __init__(self):
        self.stack = []

    def push(x):
        self.stack.append(x)

    def pop():
        if len(self.stack) <1:
            return -1
        else:
            temp = self.stack[-1]
            self.stack.pop()
            return temp
        
    def top():
        if len(self.stack) <1:
            return -1
        else:
            return self.stack[-1]
        
