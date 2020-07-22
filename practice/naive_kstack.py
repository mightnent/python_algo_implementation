"""
Naive implementation of k stack in 1 array means to divide 
the array into k equal parts and not care how each part grows.
It is probably the solution you want to code during the interview. 
input: array length and number of segments
output: array
"""
import copy

class K_stack():
    def __init__(self,n,k):
        self.arr = [None]*n
        self.interval = n//k 
        self.pointers = []
        for i in range(0,len(self.arr),self.interval):
            self.pointers.append(i)
        self.base = copy.deepcopy(self.pointers)
    
    #sn = stack number. starts from 0
    #does not return anything
    def push(self,val,sn):
        if self.arr[self.pointers[sn]]:
            self.pointers[sn] +=1
            self.arr[self.pointers[sn]] = val
        else:
            self.arr[self.pointers[sn]] = val
    
    #returns the value of item popped out
    def pop(self,sn):
        if self.arr[self.pointers[sn]]:
            tmp = self.arr[self.pointers[sn]]
            self.arr[self.pointers[sn]] = None
            self.pointers[sn] -=1
            return tmp
    
    def isFull(self,sn):
        if sn == len(self.base)-1:
            if self.arr[-1]:
                return True
        else:
            index = self.base[sn+1] - 1 
            if self.arr[index]:
                return True
            return False

    def isEmpty(self,sn):
        if sn >= len(self.base):
            return -1
        if not self.arr[self.base[sn]]:
            return True
        return False

test = K_stack(10,3)
print(test.isEmpty(2))
print(test.push(3,0))
print(test.push(5,2))
print(test.pop(2))
print(test.arr)