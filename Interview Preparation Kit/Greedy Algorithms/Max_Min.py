# You will be given a list of integers, arr, and a single integer k. You must create an array of length k 
# from elements of arr such that its unfairness is minimized. Call that array subarr. Unfairness of an array is calculated as
# max(subarr) - min(subarr)

## SOLUTION: Use sorting and then take difference of max and min values in sliding window of size k.

def maxMin(k, arr):
    n = len(arr)
    arr.sort()
    # sliding window of size k
    i = 0
    maxMin = sys.maxint
    while i <= n - k:
        cur_maxMin = arr[i+k-1] - arr[i]
        print cur_maxMin
        if cur_maxMin < maxMin:
            maxMin = cur_maxMin
        i += 1
    return maxMin
        
