
class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev