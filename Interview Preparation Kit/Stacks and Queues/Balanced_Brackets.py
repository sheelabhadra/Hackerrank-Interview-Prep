# Given  strings of brackets, determine whether each sequence of brackets is balanced. 
# If a string is balanced, return YES. Otherwise, return NO.

## SOLUTION: Use stack and a dictionary

def isBalanced(s):
    stack = []
    d = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in set(['(', '{', '[']):
            stack.append(c)
        else:
            if stack != []:
                temp = stack.pop()
                if temp != d[c]:
                    return 'NO'
            else:
                return 'NO'
        print stack
 
