# Given two strings, a and b, that may or may not be of the same length, determine the minimum number of 
# character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

# For example, if a = cde and b = dcf, we can delete e from string a and f from string b so that both remaining strings
# are cd and dc which are anagrams.

## SOLUTION:

def makeAnagram(a, b):
    d1, d2, res = [0]*26, [0]*26, [0]*26
    deletions = 0
    for c in a:
        d1[ord(c)-97] += 1
            
    for c in b:
        d2[ord(c)-97] += 1
    
    for i in range(26):
        res[i] = d1[i] - d2[i]
    
    for c in res:
        if c != 0:
            deletions += abs(c)
    
    return deletions
    
