"""
concept: binary search
requirements: 
if number in array, return the index
if number not in array, return the supposed index if number in array
input: python list / array
output: integer
edge case: None, []
assumption: ordered array, no duplicates
acknowledge the naive solution of O(n) time
"""

#using binary search
def search_insert(arr,target):
    if arr == [] or arr==None:
        return -1
    low= 0
    high = len(arr)-1
    while(low<=high):
        mid = (low+high)//2
        mid_val = arr[mid]
        if mid_val==target:
            return mid
        elif mid_val<target:
            low = mid + 1
        else:
            high = mid - 1
    return low