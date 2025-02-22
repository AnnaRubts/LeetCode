# TODO: more tests needed

class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        self.prev = None

class LRUcache:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.cache = {}
        self.capacity = capacity
    
    def put(self, key, value):
        if len(self.cache) < self.capacity:
            if key in self.cache:
                #update key with value
                self.cache[key][0] = value
                #update LRU LL
                usage_node = self.cache[key][1]
                prev = usage_node.prev
                next = usage_node.next
                if prev:
                    prev.next = next
                if next:
                    next.prev = prev
                usage_node.prev = None
                usage_node.next = self.head
                self.head.prev = usage_node
                self.head = usage_node

            else:
                usage_node = Node(key)
                self.cache[key] = [value, usage_node]
                usage_node.next = self.head
                if self.head:
                    self.head.prev = usage_node
                if not self.tail:
                    self.tail = self.head
                self.head = usage_node

        else:
            self.evict()
            self.put(key, value)
    
    def get(self, key):
        if key in self.cache:
            value = self.cache[key][0]
            #update LRU LL
            usage_node = self.cache[key][1]
            prev = usage_node.prev
            next = usage_node.next
            if prev:
                prev.next = next
            if next:
                next.prev = prev
            else:
                self.tail = usage_node.prev
            usage_node.prev = None
            usage_node.next = self.head
            self.head.prev = usage_node
            self.head = usage_node
        else:
            print(f"No key {key} in cache")
        return value
    
    def evict(self):
        lru_node = self.tail
        self.cache.pop(lru_node.key)
        self.tail = lru_node.prev
        if lru_node.prev:
            lru_node.prev.next = None
        else:
            self.head = self.prev = None


    def print_cache(self):
        for key in self.cache:
            print(key, ", ", end ="")
        print()

if __name__ == "__main__":
    myCache = LRUcache(4)
    myCache.put(1,1)
    myCache.put(2,2)
    myCache.put(3,3)
    myCache.put(4,4)
    myCache.print_cache()
    myCache.put(5,5)
    myCache.put(6,6)
    myCache.print_cache()
    myCache.get(3)
    myCache.put(7, 7)
    myCache.print_cache()