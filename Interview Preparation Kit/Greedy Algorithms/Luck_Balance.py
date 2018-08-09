# https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms&h_r=next-challenge&h_v=zen

## SOLUTION: T.C.: O(nlogn)
# Sort the array by first element and then reverse it.
# Keep decrementing k until you reach 0.
# If there are still important contests left, then deduct the luck values of important contests from the balance.
# This will ensure that the smaller luck values are deducted from the luck balance.

def luckBalance(k, contests):
    contests.sort()
    contests = contests[::-1]
    balance = 0
    print contests
    for i in range(len(contests)):
        if contests[i][1] == 1 and k != 0:
            k -= 1
            balance += contests[i][0]
        elif contests[i][1] == 1 and k == 0:
            balance -= contests[i][0]
        else:
            balance += contests[i][0]
        print balance, k
    return balance
        
