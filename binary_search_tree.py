class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if not self.root:
            self.root = new_val
            return self.root
        else:
            return self.insert_helper(self.root,new_val)
    
    def insert_helper(self,current,val):
        if current<val:
            if current.right:
                self.insert_helper(current.right,val)
            else:
                current.right = Node(val)
        else:
            if current.left:
                self.insert_helper(current.left,val)
            else:
                current.left = Node(val)

    def search(self, find_val):
        return self.search_helper(self.root,find_val)
    
    def search_helper(self,current,val):
        if current:
            if current.value == val:
                return True
            if current.value<val:
                return self.search_helper(current.right,val)
            else:
                return self.search_helper(current.left,val)
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))