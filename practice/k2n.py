import linkedlist_template as LL
ll = LL.LinkedList()
ll.add("1")
ll.add("2")
ll.add("3")
ll.add("4")
ll.add("5")

def k2n(LL,k):
    current = LL.head
    counter = 0
    while counter < k:
        current = current.next
        counter += 1
    master = []
    while current:
        master.append(current.data)
        current = current.next
    return master

print(k2n(ll,2))