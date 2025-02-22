class Node:
    def __init__(self, val=None, key=None):
        self.key = key
        self.val = val
        self.next = None

class HashMap:
    def __init__(self, size):
        self.map = [Node() for _ in range(size)] #initialize with dummy Node
        self.size = size
        self.used_indexes = set()
    
    def hash_key(self, key):
        return key%(self.size)
    
    def put(self, key, value):
        index = self.hash_key(key)
        self.used_indexes.add(index)
        curr_node = self.map[index]
        while(curr_node):
            if curr_node.key == key:
                curr_node.val = value
                return
            if not curr_node.next:
                break
            curr_node = curr_node.next
        curr_node.next = Node(value, key)
    
    def get(self, key):
        index = self.hash_key(key)
        curr_node = self.map[index]
        while(curr_node):
            if curr_node.key == key:
                return curr_node.val
            curr_node = curr_node.next
        print("Key doesnt exists")
        return None
    
    def remove(self, key):
        index = self.hash_key(key)
        curr_node = self.map[index]
        while(curr_node.next):
            if curr_node.next.key == key:
                curr_node.next = curr_node.next.next
                break
            curr_node = curr_node.next
        if not self.map[index].next and index in self.used_indexes:
            self.used_indexes.remove(index)
        print("Key doesnt exists")
        return None
    
    def printHashMap(self):
        for i in range(self.size):
            print(i, " : ", end="")
            curr_node = self.map[i]
            while(curr_node):
                print("(", curr_node.key, ",", curr_node.val, ") -> ", end="")
                curr_node = curr_node.next
            print("None")
    
    def setAll(self, value):
        for i in self.used_indexes:
            curr_node = self.map[i]
            while(curr_node):
                curr_node.val = value
                curr_node = curr_node.next


if __name__ == "__main__":
    myHashMap = HashMap(15)
    myHashMap.put(7, 1)
    myHashMap.put(3, 11)
    myHashMap.put(20, 0)
    myHashMap.put(13, 22)
    myHashMap.put(5, 80)
    myHashMap.put(30, 222)
    myHashMap.put(2, 44)
    myHashMap.put(70, 7)
    myHashMap.printHashMap()
    print(" ")
    myHashMap.put(70, 700)
    myHashMap.printHashMap()
    print(myHashMap.get(5))
    print(" ")
    myHashMap.remove(20)
    myHashMap.printHashMap()

    print(" ")
    myHashMap.setAll(777)
    myHashMap.printHashMap()