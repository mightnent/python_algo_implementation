"""
input:string
output: bool
edge case: None,"",random strings
clarification: for random strings, we need to clean them?
usually yes: remove space and turn all to lower case
approach:
mention the naive solution first then optimize from there
"""

#naive solution
def isPalinrome(s):
    s = "".join(filter(str.isalnum,s)).lower()
    return "".join(reversed(s)) == s
"""
Analysis:
time complexity is O(n)
space complexity is O(n) -> cuz temp store array
"""

#optimised pointer method. 
def isPalidrome_optimized(s):
    s = "".join(filter(str.isalnum,s)).lower()
    #left and right are pointers
    left,right = 0, len(s)-1
    while left<right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True

"""
Analysis:
only got 1 loop: O(n)
space: O(1) since only got 2 pointers
"""
