# Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
# It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters 
# will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.

## SOLUTION: Too much hardcoding. Need to find an elegant solution.

def isValid(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    print d
    
    count_list = []
    for k,v in d.items():
        count_list.append(v)
    
    nums = list(set(count_list))
    if len(nums) > 2:
        return 'NO'
    if len(nums) == 1:
        return 'YES'
    
    count1, count2 = 0, 0 
    for c in count_list:
        if c == nums[0]:
            count1 += 1
        else:
            count2 += 1
    
    if count1 != 1 and count2 == 1:
        if nums[1] == 1 or abs(nums[1] - nums[0]) == 1:
            return 'YES'
    if count2 != 1 and count1 == 1:
        if nums[0] == 1 or abs(nums[1] - nums[0]) == 1:
            return 'YES'
    
    return 'NO'
