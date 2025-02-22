from LinkedList import Node, LinkedList

def reverseLL(head: Node) -> Node:
    # no new nodes
    reversed_head = None
    while head:
        temp = head.next
        head.next = reversed_head
        reversed_head = head
        head = temp
    return reversed_head


# Hard: Recursively reverse linked-list
def reverseLLRec(head: Node) -> Node:
    # Base case: empty list or single node
    if head is None or head.next is None:
        return head
    
    # Recursively reverse the sublist starting at head.next
    new_head = reverseLLRec(head.next)
    
    # Make the next node point back to the current node
    head.next.next = head
    # Break the link from current node to the next node
    head.next = None
    
    return new_head

if __name__ == "__main__":
    # create simple linked-list
    ll = LinkedList([3, 2, 1])
    ll.printList()

    reversed_head = reverseLL(ll.head)
    reversed_head.printfromNode()

    ll2 = LinkedList([40, 30, 20])
    ll2.printList()
    reversed_head = reverseLLRec(ll2.head)
    reversed_head.printfromNode()





