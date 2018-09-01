# You will be given an array of integers and a target value. Determine the number of pairs of array elements
# that have a difference equal to a target value.

## SOLUTION: Sort the array. Then use 2 pointers to find pairs that satisfy the criteria.

def pairs(k, arr):
    arr.sort()
    n = len(arr)
    i, j = 0, 1
    count = 0
    while j < n:
        if arr[j] - arr[i] == k:
            count += 1
            i += 1
            j += 1
        elif arr[j] - arr[i] < k:
            j += 1 
        else:
            i += 1
    return count
