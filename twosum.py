arr = [1,2,3,5,6]
target = 11
def twoSums(arr,target):
    d = {}
    for i,num in enumerate(arr):
        n = target-num
        if n not in d:
            d[num] = i
        else:
            return [d[n],i]

#brute force
def twosums(arr,target):
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[i]+arr[j] == target:
        return [i,j]

"""
space complexity: O(n)
"""