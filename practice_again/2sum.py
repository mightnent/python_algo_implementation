"""
given an array, find the index of 2 numbers, in which the sum is the target
input: arr
ouput: [i,j]
clarification: no multiple pairs that can give rise to the same target
edge: None,[]
"""
def twosum(arr,target):
    if arr ==[] or arr == None:
        return 
    
    d = {}
    for ind,num in enumerate(arr):
        want = target - num
        if want not in d:
            d[want] = ind
        else:
            return [d[want],ind]
    return -1