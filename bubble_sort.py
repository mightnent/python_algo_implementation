#naive approach

arr = [21,4,1,3,9,20,25,6,21,14]

def bubble_sort(arr,iter):
    for i in range(iter):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr        