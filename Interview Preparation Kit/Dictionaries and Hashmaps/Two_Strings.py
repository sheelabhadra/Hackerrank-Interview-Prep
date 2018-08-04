# Given two strings, determine if they share a common substring. A substring may be as small as one character.

# For example, the words "a", "and", "art" share the common substring "a". The words "be" and "cat" do not share a substring.

## SOLUTION: Create a set and check the presence of common characters.

def twoStrings(s1, s2):
    common_chars = set()
    for c in s1:
        if c not in common_chars:
            common_chars.add(c)
    
    for c in s2:
        if c in common_chars:
            return 'YES'
    
    return 'NO'
