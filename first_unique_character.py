"""
given input of string : "aaron"
output should be an integer, which is the index of the first unique character
edge cases could be none, or empty string
the string input does not contain weird characters
"""

def first_unique(ip):
    if ip == None or ip == "":
        return -1
    d = {}
    ip = list(ip)
    for i in range(len(ip)):
        if ip[i] in d:
            d[ip[i]] +=1
        else:
            d[ip[i]] = 1
    for i in range(len(ip)):
        if d[ip[i]] == 1:
            return i
    return -1

"""
Analysis:
time complexity is 2n for the loops and then constant time for the hashtable-> which is just O(n)
space complexity is just O(64), since only 64 keys. which is O(1)
"""

"""
an alternative solution built upon python's string manipulation
rindex is simply the last occurance of the char
"""
def first_unique2(ip):
    if ip == None or ip == "":
        return -1
    for i,char in enumerate(ip):
        if ip.index(char) == ip.rindex(char):
            return i
    return -1

"""
Analysis:
time complexity is bad. n(n+n) -> quadratic time
space complexity is O(1)
so the code may look shorter but in fact worse off
lesson of the day: stick with hash tables
"""