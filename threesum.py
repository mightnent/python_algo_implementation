"""
given arr of integers, find a+b+c=0
else return -1
input: array of int. Can have duplicate numbers
output: 2d array. eg [[-1,0,1],[-1,2,-1]]. The output triplet needs to be unique. 
what this means is [-1,0,1] is treated as the same as [1,0,-1]
edge case: [] , return -1
"""
def threesum(arr):
    output = []
    arr.sort()
    length= len(arr)
    for i in range(length):
        #i is the first pointer
        left = i+1
        right = length -1
        #this checks for duplicate inputs
        if i>0 and arr[i-1] == arr[i]:
            continue
        #loop terminates only when the other 2 pointers cross
        while left<right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
                output.append([arr[i],arr[left],arr[right]])
                while left<right and arr[left+1] == arr[left]:
                    left+=1
                while left<right and arr[right-1]==arr[right]:
                    right -=1
                left +=1
                right -=1
            elif total<0:
                #move the left pointer right
                left +=1
            else:
                #move the right pointer to the left
                right -=1
    return output

"""
time complexity: nlogn + n^2 => O(n^2)
space complexity: depends. If you count the output array, then O(n). If not, it's just O(1) for the pointers
"""
 