# Given an array 'a' of 'n' integers and a number, 'd', perform  left rotations on the array. 
# Return the updated array to be printed as a single line of space-separated integers.

## SOLUTION: Use the same method as right rotation

def rotLeft(a, d):
    n = len(a)
    # 1. reverse the array
    a = a[::-1]
    # 2. reverse till n-d
    a[:n-d] = a[:n-d][::-1]
    # 3. reverse from n-d
    a[n-d:] = a[n-d:][::-1]
    return a
    
