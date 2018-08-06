# You are given an array and you need to find number of tripets of indices (i,j,k) such that the elements
# at those indices are in geometric progression for a given common ratio r and i<j<k.

# For example, arr = [1,4,16,64]. If r = 4, we have [1,4,16] and [4,16,64] at indices (0,1,2) and (1,2,3).

## SOLUTION: T.C.: O(n), S.C.: O(n); Passes 11/13 test cases :(
# Count number of occurences of each item in the array using a dict.
# Number of triplets will be (#it) x (#r*it) x (#r*r*it) if all the 3 items are in the dict.
# Take care of the case when r = 1.

def countTriplets(arr, r):
    d = {}
    for it in arr:
        if it in d:
            d[it] += 1
        else:
            d[it] = 1
    
    s = set(arr)
    count = 0
    
    if r == 1:
        for it in s:
            if d[it] > 2:
                count += math.factorial(d[it])/(math.factorial(3)*math.factorial(d[it]-3))
                
    else:
        for it1 in s:
            it2 = r*it1
            if it2 in s:
                it3 = r*it2
                if it3 in s:
                    count += d[it1]*d[it2]*d[it3]
    return count
    
