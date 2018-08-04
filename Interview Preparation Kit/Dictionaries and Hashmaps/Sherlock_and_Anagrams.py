# Two strings are anagrams of each other if the letters of one string can be rearranged to 
# form the other string. Given a string, find the number of pairs of substrings of the string which are anagrams of each other.

# For example s = mom, the list of all anagrammatic pairs is [m,m], [mo, om] at positions [[0],[2]], [[0,1],[1,2]]respectively.

## SOLUTION: O(n2logn)
# Check substrings of all sizes. Use sorted string as key.
# For every key there would be n*(n-1) combinations of valid anagrams

def sherlockAndAnagrams(s):
    n = len(s)
    dict = {}
    count = 0
    for i in range(n):
        for j in range(n-i):
            temp =  str(sorted(s[j:j+i+1]))
            if temp in dict:
                dict[temp] += 1
            else:
                dict[temp] = 1
    
    for k in dict:
        count+=dict[k]*(dict[k]-1)//2
    
    return count
