# Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. 

def countSwaps(a):
    n = len(a)
    numSwaps = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                numSwaps += 1
    print "Array is sorted in {} swaps.".format(numSwaps)
    print "First Element: {}".format(a[0])
    print "Last Element: {}".format(a[-1])
                
