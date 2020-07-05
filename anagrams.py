"""
complete anagrams are words that contains exactly the same letters, though need not be in the same order
example: tea and eat
question definition:
group all the anagrams tgt
input : list of strings
output: 2D array with each sub array being a group of anagram
edge case: None or []
clarification: complete anagrams? yes
"""
def anagrams(arr):
    d={}
    master = []
    for i in arr:
        key = "".join(sorted(i))
        if key in d:
            d[key].append(i)
        else:
            d[key] = [i]
    for val in d.values():
        master.append(val)
    return master

"""
Analysis:
time complexity: n*(mlogm)
n is the arr length and m is the string length. 
mlogm is the default sort in python
space complexity: worse case is all unique, so O(n)
"""
