"""
find out how many levels a tree has
input: root
output: int

hint: stack
think bottom up
"""

class max_depth():
    def max_depth(self,node):
        if not node:
            return 0
        return 1 + max(self.max_depth(node.left),self.max_depth(node.right))
