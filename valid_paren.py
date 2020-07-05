"""
input: 6 char string : "(){}[]"
output: bool
edge: "", None
clarify, for "", do you return true or false -> in this case, return true
must be in correct order and type to be true
"""

"""
pseudo code
for char in str
if opening, push to stack
if close, pop and compare
if fail, return
if all pass
"""
def valid_parenthesis(s):
    if s=="":
        return True
    if s==None:
        return False
    stack = []
    for i in s:
        if i=="(" or i=="{" or i=="[":
            stack.append(i)
        else:
            if  len(stack)==0:
                return False
            if i==")" or i=="}" or i=="]":
                last = stack.pop()
                if last == "(" and i !=")":
                    return False
                if last == "{" and i!="}":
                    return False
                if last == "[" and i!="]":
                    return False
    if len(stack)>0:
        return False
    return True

"""
Analysis:
time complexity: O(n)
space complexity: O(n)
"""
