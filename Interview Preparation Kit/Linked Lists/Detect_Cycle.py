# Check if there's a cycle in a Linked List.

## SOLUTION:

def has_cycle(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
    
