# Implement two Stacks in an Array
# Create a data structure twoStacks that represent two stacks.
#  Implementation of twoStacks should use fixed size,
#  Push and Pop should be O(1).

class TwoStacks:
    def __init__(self, capacity):
        self.stack = [0]*capacity
        self.p_stack1 = 0
        self.p_stack2 = capacity-1
    
    def push(self, val, stack_num):
        if self.p_stack1 <= self.p_stack2:
            if stack_num == 1:
                self.stack[self.p_stack1] = val
                self.p_stack1 += 1
            else:
                self.stack[self.p_stack2] = val
                self.p_stack2 -= 1
        else:
            print("Error: Stacks are full")
    
    def pop(self, stack_num):
        if stack_num == 1 and self.p_stack1 > 0 :
            res = self.stack[self.p_stack1-1]
            self.stack[self.p_stack1-1] = 0
            self.p_stack1 -= 1
            return res
        elif self.p_stack2 < len( self.stack)-1 :
            res = self.stack[self.p_stack2+1]
            self.stack[self.p_stack2+1] = 0
            self.p_stack2 += 1
            return res
        else:
            print("Error: Stack are empty")
    
    def print_stack(self):
        print(self.stack)
    
if __name__ == "__main__":
    myStack = TwoStacks(7)
    myStack.print_stack()
    myStack.push(20, 1)
    myStack.push(40, 1)
    myStack.push(9, 2)
    myStack.print_stack()
    myStack.push(100, 1)
    myStack.push(7, 2)
    myStack.push(5, 2)
    myStack.push(3, 2)
    myStack.print_stack()
    myStack.push(30, 2)
    print(myStack.pop(1))
    print(myStack.pop(1))
    myStack.print_stack()
    print(myStack.pop(2))
    myStack.print_stack()





    
        


