#give up on bottom up, will come back to it again in the future
arr = [21,4,1,3,9,20,25]
import copy
class mergesort_BU():
    def __init__(self,arr):
        self.arr = arr
    
    def sorting(self,arr):
        n = len(arr)
        aux = [None]*n
        leng = 1
        while leng<n:
            for low in range(0,n-leng,leng+leng):
                mid = low+len-1
                high = min(low+leng+leng-1,n-1)
                merge(arr,aux,low,mid,high)

            leng *= 2
    
    def merge(self,arr,aux,low,mid,high):
        for k in range(low,high+1):
            pass




