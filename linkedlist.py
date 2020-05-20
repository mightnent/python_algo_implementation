class LinkedList():
    def __init__(self):
        self.length = 0
        self.head = None
    
    class Node():
        def __init__(self,data):
               self.data = data
               self.next = None

    def size(self):
        return self.length

    def getHead(self):
        return self.head

    def add(self,data):
        node = self.Node(data) 
        if self.head == None:
            self.head = node
        else:
            currentNode = self.head
            while(currentNode.next != None):
                currentNode = currentNode.next
            #after breaking out of while loop, it means
            #it has reached the end of linked list
            currentNode.next = node
        self.length+=1
    
    def remove(self,data):
        currentNode = self.head
        previousNode = None

        if currentNode.data == data:
            #it can be null or the next node's data
            head = currentNode.next
        else:
            while(currentNode.data != data):
                previousNode = currentNode
                currentNode = currentNode.next
            previousNode.next = currentNode.next
        self.length -= 1
    
    def isEmpty(self):
        return self.length == 0
    
    def indexOf(self,data):
        currentNode = self.head
        #-1 to indicate this data does not exist
        index = -1
        while(currentNode != None):
            index +=1
            if currentNode.data == data:
                return index
            currentNode = currentNode.next
        
        return -1

    def elementAt(self,index):
        currentNode = self.head
        count = 0
        while(count < index):
            currentNode = currentNode.next
            count += 1
        return currentNode.data
    
    def addAt(self,index,data):
        node = self.Node(data)
        currentNode = self.head
        previousNode = None
        currentIndex = 0

        if index > self.length:
            return False
        
        if index == 0:
            node.next = currentNode
            self.head = node
        else:
            while(currentIndex<index):
                previousNode = currentNode
                currentNode = currentNode.next
                currentIndex +=1
            previousNode.next = node
            node.next = currentNode
        self.length +=1
    
    def removeAt(self,index):
        currentNode = self.head
        currentIndex = 0
        previousNode = None

        if(index<0 or index>self.length):
            return False
        if index == 0:
            self.head = currentNode.next
        else:
            while(currentIndex < index):
                previousNode = currentNode
                currentNode = currentNode.next
                currentIndex +=1
            previousNode.next = currentNode.next
        self.length -=1
        return currentNode.data

    def getList(self):
        linkedlist = []
        currentNode = self.head
        while(currentNode != None):
            linkedlist.append(currentNode.data)
            currentNode = currentNode.next
        return linkedlist
    
    def __str__(self):
        return ", ".join(x for x in self.getList())
        
conga = LinkedList()
conga.add('Kitten')
conga.add('Puppy')
conga.add('Dog')
conga.add('Cat')
conga.add('Fish')
print(conga.size())
print(conga.removeAt(3))
print(conga.elementAt(3))
print(conga.indexOf('Puppy'))
print(conga.size())