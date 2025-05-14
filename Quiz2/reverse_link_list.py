def reverseList(head: ListNode) -> ListNode:

    prev = None       # Previous node starts as None
    current = head    # Start with current node at head
    
    while current:
        # Store next node before we overwrite current.next
        next_node = current.next
        # Reverse the link
        current.next = prev
        # Move pointers forward
        prev = current
        current = next_node
    
    # Prev will be the new head at the end
    return prev