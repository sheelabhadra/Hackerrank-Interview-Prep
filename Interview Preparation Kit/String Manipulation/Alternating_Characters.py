# You are given a string containing characters A and B only. Your task is to change it into a string 
# such that there are no matching adjacent characters. To do this, you are allowed to delete zero or
# more characters in the string.

# Your task is to find the minimum number of required deletions.

## SOLUTION:

def alternatingCharacters(s):
    i, n = 0, len(s)
    count = 0
    while i < n-1:
        if s[i] == s[i+1]:
            count += 1
        i += 1
    return count
    
