arr = [0,0,1,1,3,4,5,5]

def count_unique(nums):
    if len(nums) == 0:
        return 0
    i,j = 0,1
    for j in range(1,len(nums)):
        if nums[i] != nums[j]:
            i+=1
            nums[i] = nums[j]
    return i+1