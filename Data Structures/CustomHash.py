# Design a custom datastructure that can store numbers like a dynamically sized array and supports all of the following operations
# get(int index)
# set(int idx, int value)
# setAll(int value)

class CustomHash:
    def __init__(self):
        self.dict = {}
        self.set_all_value = None
        self.set_all_time = 0
        self.curr_time = 1
    
    def get(self, key):
        if key in self.dict:
            if self.dict[key][1] > self.set_all_time:
                return self.dict[key][0]
            else:
                return self.set_all_value
        else:
            return None
        
    def set(self, key, value):
        self.dict[key] = [value, self.curr_time]
        self.curr_time+=1
    
    def setAll(self, value):
        self.set_all_value = value
        self.set_all_time = self.curr_time
        self.curr_time+=1



if __name__ == "__main__":
    myHash = CustomHash()
    myHash.set(1, 1)
    myHash.set(2, 2)
    print(myHash.get(1))
    print(myHash.get(2))
    myHash.setAll(3)
    print(myHash.get(1))
    print(myHash.get(2))
    myHash.set(1, 4)
    print(myHash.get(1))
    print(myHash.get(2))
    myHash.setAll(5)
    print(myHash.get(1))
    print(myHash.get(2))

    