class ListNode:
     def __init__(self, val):
        self.val: int = val
        self.next: ListNode = None


# T = O(n), S = O(1)
def traverse(node: ListNode):
    
    # node != None
    while node:
        node = node.next

# T = O(1), S = O(1)
def insert_at_head(head: ListNode, val: int) -> ListNode:
    new_node = ListNode(val)

    new_node.next = head
    return new_node

# T = O(n), S = O(1)
def insert_at_tail(head: ListNode, val: int) -> ListNode:
    new_node = ListNode(val)
    
    traverse(head)
    
    head.next = new_node
    return new_node
    
    

head = ListNode(1)

head = insert_at_head(head, 0)
                     # 1
tail = insert_at_tail(head.next, 2)

assert(head.val, head.next.val, head.next.next.val, head.next.next.next) == (0, 1, 2, None)
    
    





