# You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without any duplicates.
# You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array 
# in ascending order.

## SOLUTION: T.C.: O(n)

def minimumSwaps(arr):
    n = len(arr)
    minSwaps = 0
    i = 0
    
    while i < n-1:
        if (i+1) != arr[i]:
                lo = i
                hi = arr[i] - 1
                minSwaps += 1
                arr[lo], arr[hi] = arr[hi], arr[lo]
                if (arr[i] - 1) <= i:
                    i = arr[i] - 1
                    continue
        i += 1
    return minSwaps
    
