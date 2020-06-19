class Queue:
    def __init__(self):
        self.storage = []
        #the Q will look like [(1, 1), (1, 2), (1, 3)]

    #higher the number, greater the priority
    def enqueue(self, priority,new_element):
        if not self.storage:
            self.storage.append((priority,new_element)) 
        else:
            for i in range(len(self.storage)):
                if priority>=self.storage[i][0]:
                    continue
                    
                else:
                    self.storage.insert(i,(priority,new_element))
                    return
                
            self.storage.append((priority,new_element))

    #peek just look at the head
    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)
    
q = Queue()
q.enqueue(1,2)
q.enqueue(1,4)
q.enqueue(1,5)
q.enqueue(2,5)
q.enqueue(2,6)
q.enqueue(4,1)
q.enqueue(1,6)
