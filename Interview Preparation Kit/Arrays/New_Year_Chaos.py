# WAP to find the minimum number of bribes (swaps) that took place to get the queue into its current state!
# e.g. 1 2 3 4 5 --> 2 1 5 3 4 => min bribes = 3

def minimumBribes(q):
    n = len(q)
    for i in range(n):
        diff = q[i] - (i+1)
        if diff > 2:
            print "Too chaotic"
            return
    
    res = 0
    swapped = False
    # Bubble sort to find number of swaps
    for i in range(n-1):
        for j in range(n-1):
            if q[j] > q[j+1]:
                res += 1
                q[j], q[j+1] = q[j+1], q[j]
                swapped = True
            
        if swapped:
            swapped = False
        else:
            break
    print res
    return res
        
