"""
determine if binary tree is height balanced
input: binary tree
output: bool
edgecase: None, return True
"""

class TreeNode():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class IsBalanced():
    def is_balanced(self,node):
        if not node:
            return True
        height_diff = abs(self.get_depth(node.left) - self.get_depth(node.right))
        return height_diff <=1 and self.is_balanced(node.left) and self.is_balanced(node.right)


    def get_depth(self,node):
        if not node:
            return 0
        return 1 + max(self.get_depth(node.left),self.get_depth(node.right))

"""
analysis:
time complexity: get_depth is O(n) and is_balanced is also O(n). Hence, this is a O(n^2) run time
space complexity: O(n) for worst case, since that is just a linked list. 
note:space complexity is about stack frames
"""
