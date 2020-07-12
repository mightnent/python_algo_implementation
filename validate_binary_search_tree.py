"""
check for BST: left<right
input: binary tree
output: bool
edgecase: root = None: return true
if 2 equal values: return false

hint: preorder traversal
need to have a new min max at each recursion
"""
class TreeNode():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class validate():
    def val_BST(self,node,lower=float('-inf'),upper=float('inf')):
        if not node :
            return True
        if node.value <= lower or node.value>=upper:
            return False
        return self.val_BST(node.left,lower,node.val) and self.val_BST(node.right,node.value,upper)

