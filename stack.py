# push(val) - pushes the element val into the stack
# pop() - removes the element on the top of the stack
# top() - gets the top element of the stack

class Stack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, val):
        self.stack.append(val)
        
    def pop(self):
        self.stack.pop(-1)
        
    def top(self):
        return self.stack[-1]
