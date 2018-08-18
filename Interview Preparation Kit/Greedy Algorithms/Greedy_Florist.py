# A group of friends want to buy a bouquet of flowers. The florist wants to maximize his number of new customers 
# and the money he makes. To do this, he decides he'll multiply the price of each flower by the number of that 
# customer's previously purchased flowers plus . The first flower will be original price, , the next will be  and so on.

# Given the size of the group of friends, the number of flowers they want to purchase and the original prices
# of the flowers, determine the minimum cost to purchase all of the flowers.

## SOLUTION: Sort the price/cost array in decreasing order.
# First buy the expensive flowers and then buy the cheaper ones in the subsequent iterations

def getMinimumCost(k, c):
    n = len(c)
    c.sort()
    c = c[::-1]
    minCost = 0
    if n%k == 0:
        iters = n/k
    else:
        iters = n//k + 1
    
    for it in range(iters):
        for fr in range(k):
            curr_idx = it*k + fr
            if curr_idx == n:
                return minCost
            minCost += (it + 1)*c[curr_idx]
    return minCost
    
