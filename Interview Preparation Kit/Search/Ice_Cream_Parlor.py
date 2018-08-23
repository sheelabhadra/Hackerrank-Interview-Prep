# Given the value of money and the cosy of each flavor for  trips to the Ice Cream Parlor, 
# help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money during each visit.

## SOLUTION: Create a new array that contains tuple of cost and index.
# Sort the tuple and then apply 2 pointer technique find the pairs
# T.C.: O(nlogn); S.C.: O(n)

def whatFlavors(cost, money):
    cost_tup = [(cost[i],i) for i in range(len(cost))]
    cost_tup.sort()

    i, j = 0, len(cost)-1
    while i < j:
        if cost_tup[i][0] + cost_tup[j][0] < money:
            i += 1
        elif cost_tup[i][0] + cost_tup[j][0] > money:
            j -= 1
        else:
            if cost_tup[i][1] < cost_tup[j][1]:
                print str(cost_tup[i][1]+1) + ' ' + str(cost_tup[j][1]+1)
            else:
                print str(cost_tup[j][1]+1) + ' ' + str(cost_tup[i][1]+1)
            return
