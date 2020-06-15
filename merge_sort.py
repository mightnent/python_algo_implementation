class MergeSort():
    
    def merge(self,left,right,A):
        nL = len(left)
        nR = len(right)
        i=0
        j=0
        k=0
        while(i<nL and j<nR):
            if left[i]<right[j]:
                A[k] = left[i]
                i+=1
            else:
                A[k] = right[j]
                j+=1
            k+=1
        while i<nL:
            A[k] = left[i]
            i+=1
            k+=1
        while j<nR:
            A[k] = right[j]
            j+=1
            k+=1
    
    def merge_sort(self,A):
        n = len(A)
        if n<2:
            return
        mid = n//2
        left = [None] * mid
        right = [None] * (n-mid)
        for i in range(mid):
            left[i] = A[i]
        for i in range(mid,n):
            right[i-mid] = A[i]
        self.merge_sort(left)
        self.merge_sort(right)
        self.merge(left,right,A)
        return A

A = [9,5,3,2,7,8,4,1,6,10]
