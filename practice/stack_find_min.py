"""
design stack such that finding min is O(1) time
instead of implementing LL, use deque for py
"""
from collections import deque

class custom_stack():
    def __init__(self):
        self.stack = deque()
        self.m = 0
    
    def append(self, x):
        if len(self.stack) == 0:
            self.m = x
        elif x < self.m:
            self.m = x
        self.stack.append(x)

    def minimum(self):
        return self.m


cs = custom_stack()
cs.append(2)
cs.append(5)
print(cs.minimum())
