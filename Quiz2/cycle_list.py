class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    

    # Edge case: empty list or single node without cycle
    if not head or not head.next:
        return False
    
    # Initialize two pointers - slow moves 1 step, fast moves 2 steps
    slow = head
    fast = head.next
    
    # Loop until pointers meet or fast reaches end
    while slow != fast:
        # If fast reaches end, no cycle exists
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    # If loop exited because slow == fast, cycle exists
    return True