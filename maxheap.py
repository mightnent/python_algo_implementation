import math
class MaxHeap():
    def __init__(self):
        self.heap = [None]
    
    def insert(self,num):
        tmp = 0
        self.heap.append(num)
        if len(self.heap) > 2:
            idx = len(self.heap) -1
            while(self.heap[idx]>self.heap[math.floor(idx/2)]):
                if(idx>=1):
                    tmp = self.heap[math.floor(idx/2)]
                    self.heap[math.floor(idx/2)] = self.heap[idx]
                    self.heap[idx] = tmp
                    if math.floor(idx/2) >1 :
                        idx = math.floor(idx/2)
                    else:
                        break
    
    def remove(self):
        biggest = self.heap[1]
        if len(self.heap) > 2:
            self.heap[1] = self.heap.pop()
            if len(self.heap) ==3:
                if self.heap[1] > self.heap[2]:
                    tmp = self.heap[1]
                    self.heap[1] = self.heap[2]
                    self.heap[2] = tmp
                return biggest
            i = 1
            left = 2 * i
            right = 2 * i + 1
            while(self.heap[i] <= self.heap[left] or self.heap[i] <= self.heap[right]):
                if self.heap[left] > self.heap[right]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[left]
                    self.heap[left] = tmp
                    i = 2 * i
                else:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[right]
                    self.heap[right] = tmp
                    i = i *2 +1

                left = 2 * i
                right = 2 * i +1

                '''
                We can do perform the following check because the last element we pop and 
                assign to first index is not the smallest
                '''
                try:
                    self.heap[left] or self.heap[right]
                except:
                    break
                
        elif len(self.heap) == 2:
            self.heap.pop()
        else:
            return None
        return biggest

    def sort(self):
        result = []
        while(len(self.heap)>1):
            result.append(self.remove())
        return result

    def size(self):
        return len(self.heap)
    
    def display(self):
        return self.heap


heap = MaxHeap()
heap.insert(20)
heap.insert(19)
heap.insert(17)
heap.insert(34)