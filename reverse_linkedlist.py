"""
reverse a singly linkedlist
tail become head and head become tail
input:linkedlist
output: head of new linkedlist
edge case: only head
assumption: at least a headnode
"""

def iter_reverse(ll):
    current = ll.head
    prev = None
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev

def rec_reverse(current,prev=None):
    if current is None:
        return prev
    nxt = current.next
    current.next = prev
    return rec_reverse(nxt,current)
"""
since it is tail recursion, it does not need to wait for stack frame to finish to bubble up.
so python will discard the stack frame after each call. hence, space complexity can still be O(1)
time complexitiy is O(n)
"""