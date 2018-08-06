# Print the largest (maximum) hourglass sum found in arr.

## SOLUTION: Use list comprehension to slice multidimensional array in Python

def hourglassSum(arr):
    sum_array = []
    for i in range(4):
        for j in range(4):
            window = [arr[r][j:j+3] for r in range(i,i+3)]
            window_sum = sum(sum(row) for row in window)
            window_sum -= (window[1][0] + window[1][2])
            sum_array.append(window_sum)
    return max(sum_array)
    
