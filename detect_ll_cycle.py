"""
detect linkedlist cycle
input: ll
output: bool
assume: at least 1 node
edge case: one node
"""

##########
import LinkedList_udacity as ll
new_ll=ll.LinkedList()
e1 = ll.Element(1)
e2 = ll.Element(2)
e3 = ll.Element(3)
e4 = ll.Element(4)
e5 = ll.Element(5)
e6 = ll.Element(6)
new_ll.append(e1)
new_ll.append(e2)
new_ll.append(e3)
new_ll.append(e4)
new_ll.append(e6)
new_ll.append_loop(e5,2)
##########


def hasCycle(ll):
    current = ll.head
    nodes = set()
    while current:
        if current in nodes:
            return True
        nodes.add(current)
        current = current.next
    return False
"""
this is pretty naive solution. 
O(n) time and space
"""
#floyd's algo/tortise and hare
def hasCycle_optimized(ll):
    current = ll.head
    slow = current
    fast = current
    while fast or fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
