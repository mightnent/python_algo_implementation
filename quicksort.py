def quicksort(arr,start,end):
    if start >= end:
        return
    pIndex = partition(arr,start,end)
    quicksort(arr,start,pIndex-1)
    quicksort(arr,pIndex+1,end)

def partition(arr,start,end):
    pivot = arr[end]
    pIndex = start
    for i in range(start,end):
        if arr[i] <=pivot:
            arr[i],arr[pIndex] = arr[pIndex],arr[i]
            pIndex +=1
    arr[pIndex],arr[end] = arr[end],arr[pIndex]
    return pIndex

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
A = [7,2,1,6,8,5,3,4]
# (quicksort(A,0,7))
# print(A) 
(quicksort(test,0,9))
print(test) 