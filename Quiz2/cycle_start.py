def detectCycle(head: ListNode) -> ListNode:

    # Edge case: empty list or single node without cycle
    if not head or not head.next:
        return None
    
    # Initialize two pointers
    slow = head
    fast = head
    has_cycle = False
    
    # First phase: detect if cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # If pointers meet, cycle exists
        if slow == fast:
            has_cycle = True
            break
    
    # If no cycle found, return None
    if not has_cycle:
        return None
    
    # Second phase: find the cycle start
    # Reset slow to head, keep fast at meeting point
    # Move both at same speed until they meet again
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    # The node where they meet is the cycle start
    return slow