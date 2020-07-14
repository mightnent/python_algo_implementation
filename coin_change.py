"""
Given coins of diff denomination and a targeted amt, compute the least number of coin needed to make up amt.
if not combination available, return -1
input: arr of numbers and int amt
output: int number of coin
assumption: no duplicate coin value in input, no negative or 0 coin
"""
def coin_change(arr,amt):
    dp = [0] + ([float('inf')] * amt)
    for i in range(len(dp)):
        for j in arr:
            if j<=i:
                dp[i] = min(dp[i],dp[i-j]+1)
    
    min_coin = dp[-1]

    if min_coin == float('inf'):
        return -1
    
    return min_coin

"""
analysis:
outer loop n, where n is number amt
inner loop k, where k is the number of unique coins
hence, time complexity is O(n*k)

space complexity: O(n)
"""