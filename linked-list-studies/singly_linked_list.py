class ListNode:
     def __init__(self, val):
        self.val: int = val
        self.next: ListNode = None


# T = O(n), S = O(1)
def traverse(head: ListNode):
    
    # head != None
    while head:
        head = head.next

# T = O(1), S = O(1)
def insert_at_head(head: ListNode, val: int) -> ListNode:
    new_node = ListNode()
    new_node.val = val
    new_node.next = head
    return new_node

# T = O(n), S = O(1)
def insert_at_tail(head: ListNode, val: int) -> ListNode:
    pass





