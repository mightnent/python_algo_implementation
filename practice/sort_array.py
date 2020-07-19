"""
input: array of int
output: array of int, in ascending order
edge: []
"""

class Solutions():
    def sort_arr(self,arr):
        return self.merge_sort(arr)
    
    def merge_sort(self,arr):
        if len(arr) <= 1:
            return arr
        
        #find a mid
        mid = len(arr) // 2
        #include start but not end
        left = arr[:mid]
        right = arr[mid:]

        #division till one block
        left = self.merge_sort(left)
        right = self.merge_sort(right)

        #putting them tgt
        block = []
        #init 2 pointer
        l = r = 0
        #advancing pointers on each block
        while l < len(left) and r < len(right):
            #ascending order
            if left[l] < right[r]:
                block.append(left[l])
                l+=1
            else:
                block.append(right[r])
                r+=1
        
        #so if there's still some lefover from the left 
        if l<len(left):
            block+= left[l:]
        elif r<len(right):
            block+= right[r:]

        return block

"""
Analysis:
time complexity: O(nlogn)
why? the logn comes from the division by 2. the n comes from looking at n items for the while pointer
space complexity: O(n)
why? n/2 + n/4 + n/8 + ... -> n
"""