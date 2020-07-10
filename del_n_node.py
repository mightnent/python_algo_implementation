"""
essentially a linkedlist question
input: linkedlist, int of n
output: linkedlist, int of val of head
edgecase: del from first or last node
assumption: linkedlist at least 1 node, n is zero indexed
"""

class ListNode():
    def __init__(self,value):
        self.val = value
        self.next = None

class LinkedList():
    def __init__(self,head):
        self.head = head

    def append(self, new_node):
        #local var current, which is set to class variable self.head
        current = self.head
        #bool check if self.head is not none
        if self.head:
            #bool check if current.next is not none
            while current.next:
                #travel along pointer of to current.next, which essentially is 
                #the next element's value field. 
                current = current.next
            #break out of while loop when you reach the end of the linkedlist
            current.next = new_node
        else:
            #since self.head is none, we just declare the new_element as self.head
            self.head = new_node

def del_n_node(LL,n):
    current = LL.head
    prev = None
    counter = 0
    if n == 0:
        LL.head = current.next
        return LL.head
    while counter < n:
        prev = current
        current = current.next
        if not current:
            return -1
        counter+=1
    prev.next = current.next
    return LL.head
        
e1 = ListNode(1)
e2 = ListNode(2)
e3 = ListNode(3)
e4 = ListNode(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)

del_n_node(ll,2)
print(ll.head.val)
print(ll.head.next.val)
print(ll.head.next.next.val)