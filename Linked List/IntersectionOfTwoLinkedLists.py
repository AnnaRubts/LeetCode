from LinkedList import Node, LinkedList

# Given the heads of two singly linked-lists headA and headB,
#  return the node at which the two lists intersect.
#  If the two linked lists have no intersection at all, return null.

def getIntersectionNode(headA, headB):
    # with extra space
    seen_nodes = set()
    while (headA):
        seen_nodes.add(headA)
        headA= headA.next
    while (headB):
        if headB in seen_nodes:
            return headB
        headB= headB.next
    
    return None

#TODO: complete this solution
# Medium: with O(1) space
def getIntersectionNodeLight(headA, headB):
    # if we had the length of the linked lists, we would know from where to start the pointers
    # we can either count lengths and starts pointers from updated positions (to equalize the pointers)
    # or we can use this fact and use the trick:
    # p1 = p1.next if p1 else headB
    # p2 = p2.next if p2 else headA
    pass
   

if __name__ == "__main__":
    # create simple linked-list
    ll = LinkedList([3, 2, 1])
    
    headA = Node(0)
    headA.next = ll.head
    headB = Node(-2)
    headB.next = ll.head

    print((getIntersectionNode(headA, headB)).val)
