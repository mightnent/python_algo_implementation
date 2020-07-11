"""
given a binary tree, return the level order traversa of its node's values
i.e, breadth first 
input: binary tree root
output: 2d array
edge case: root = None, return []

hint: queue and bookmark
"""

class TreeNode():
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

class Level_Order_Traversal():
    def level_order(self,root):
        levels = []
        Q = [root]
        while Q:
            size = len(Q)
            level = []
            while size != 0:
                item = Q.pop(0)
                level.append(item.val)
                if item.left:
                    Q.append(item.left)
                if item.right:
                    Q.append(item.right)
                size -= 1
            levels.append(level)
        return levels