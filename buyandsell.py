"""
array which i-th element is the price of given stock on day i
only permitted to buy one and sell one share of the stock
input: arr
output: int. (this is the profit)
edge: if arr in descending order, return 0
hint: pointer
"""

def buy_sell(arr):
    low = arr[0]
    profit = 0
    for i in arr:
        if i < low:
            low = i
        current = i - low
        if current > profit:
            profit = current
    return profit

arr = [7,1,5,3,6,4]

"""
analysis:
time complexity: O(n), since you check every element
space complexity: O(1). You only created 3 extra var.
"""