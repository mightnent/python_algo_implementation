"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

#definition for Element in the linkedlist, or what others call a node
#each element has 2 fields, value and next(which is the pointer)
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    #this just give self.head a default value of none if nothing is passed in
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
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
            current.next = new_element
        else:
            #since self.head is none, we just declare the new_element as self.head
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        if position<1:
            return None
        #while current is not None and counter <=position
        while current and counter <= position:
            if counter == position:
                return current
            
            current = current.next
            counter += 1
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position < 1:
            return
        elif position == 1:
            #since there's only the head element in the linkedlist,
            #we simply make the new_element the head
            new_element.next = current
            self.head = new_element
        else:
            #since we are definitely not inserting in pos 1,
            #we can safely asumme that there will be a previous element
            prev = self.get_position(position-1)
            nxt = self.get_position(position)
            prev.next = new_element
            new_element.next = nxt
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        prev = None
        #we loop through to find the value that matches element value
        while current.value != value and current.next:
            prev = current
            current = current.next
        #there is a match!
        if current.value == value:
            #having a prev means "current" is definitely not the head
            if prev:
                prev.next = current.next
            #the only case is "current" being the head
            else:
                self.head = current.next
        

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print (ll.head.next.next.value)
# Should also print 3
print (ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print (ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print (ll.get_position(1).value)
# Should print 4 now
print (ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)