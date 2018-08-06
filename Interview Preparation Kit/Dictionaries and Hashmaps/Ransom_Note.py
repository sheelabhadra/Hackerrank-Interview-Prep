# Given the words in the magazine and the words in the ransom note, 
# print Yes if he can replicate his ransom note exactly using whole words from the magazine; 
# otherwise, print No.

## SOLUTION: Use dictionary to store words in the magazine

def checkMagazine(magazine, note):
    mag_dict = {}
    for w in magazine:
        if w in mag_dict:
            mag_dict[w] += 1
        else:
            mag_dict[w] = 1
    
    for w in note:
        if w in mag_dict:
            if mag_dict[w] == 0:
                print 'No'
                return
            else:
                mag_dict[w] -= 1
        else:
            print 'No'
            return
    print 'Yes'
    
