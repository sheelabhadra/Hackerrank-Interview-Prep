# Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? 
# For example, if prices = [1,2,3,4] and Mark has k = 7 to spend, he can buy items [1,2,3] for 6, 
# or [3,4] for 7 units of currency. He would choose the first group of 3 items.

## SOLUTION: Check the case when all the items in the list are included in the running sum

def maximumToys(prices, k):
    prices.sort()
    sum_it = 0
    for it in range(len(prices)):
        if sum_it <= k:
            sum_it += prices[it]
        else:
            return it-1
    return it
