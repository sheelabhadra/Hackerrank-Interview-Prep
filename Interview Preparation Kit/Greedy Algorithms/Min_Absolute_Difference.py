# Given an array of integers, find and print the minimum absolute difference between any two elements in the array.

## SOLUTION: Sort and then find minimum absolute deviation between consecutive elements.

def minimumAbsoluteDifference(arr):
    arr.sort()
    mad = sys.maxint
    for i in range(n-1):
        diff = abs(arr[i] - arr[i+1])
        if diff < mad:
            mad = diff
    return mad
