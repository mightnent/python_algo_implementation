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

"""
time complexity: O(n)
space complexity: O(k), where k is the height of tree (for the call stack)
"""

#using bfs level order traversal
class max_depth_bfs():
    def max_depth_bfs(self,root):
        if not root : return 0
        q = [root]
        depth = 0
        while q:
            size = len(q)
            depth +=1
            while size>0:
                item = q.pop(0)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
                size -=1
        return depth   

"""
time complexity: O(n)
space complexity: O(n)
"""
