# general double linked list implementation

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None
    
    def printfromNode(self):
        curr_node = self
        while(curr_node):
            print(curr_node.val, "-> ", end="")
            curr_node = curr_node.next
        print("None")

class LinkedList:
    # Note: Python does not support traditional function overloading like languages such as C++ or Java.
    #  In this example, each subsequent definition of the __init__ method overwrites the previous one, so only the last one is effective.
    # def __init__(self):
    #     self.head = None
    
    # def __init__(self, val):
    #     self.head = Node(val)
    
    def __init__(self, list):
        self.head = None
        for val in list:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
    
    def addNode(self, new_node):
        # adds node to front of LL
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def printList(self):
        curr_node = self.head
        while(curr_node):
            print(curr_node.val, "-> ", end="")
            curr_node = curr_node.next
        print("None")
  
#TODO: implement the double linked list
class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = self.head


if __name__ == "__main__":
    # create simple linked-list
    head = LinkedList([3, 2, 1])
    head.printList()

    head2 = LinkedList([])
    head2.addNode(Node(30))
    head2.addNode(Node(20))
    head2.printList()