# Two Stacks Follow-up: generalized the solution for N stacks

class NStacks:
    def __init__(self, capacity, stacks_num):
        self.stack = [(0,0)]*capacity
        self.curr_tops = [-1]*stacks_num
        self.available_positions = set()
        for i in range(capacity):
            self.available_positions.add(i)
    
    def push(self, val, stack_num):
        stack_num -= 1
        if len(self.available_positions):
            available_pos = self.available_positions.pop()
            self.stack[available_pos] = (val, self.curr_tops[stack_num])
            self.curr_tops[stack_num] = available_pos
        else:
            print(f"Error: Stack are full")
    
    def pop(self, stack_num):
        stack_num -= 1
        if self.curr_tops[stack_num] != -1:
            stack_top = self.curr_tops[stack_num]
            val, prev_ind = self.stack[stack_top]
            self.stack[stack_top] = (0, 0)
            self.available_positions.add(stack_top)
            self.curr_tops[stack_num] = prev_ind
            return val
        else:
            print(f"Error: Stack {stack_num} is empty")
    
    def print_stack(self):
        print("[" , end="")
        for v, i in self.stack:
            print(v, " " , end="")
        print("]")    

if __name__ == "__main__":
    myStack = NStacks(6, 3)
    myStack.print_stack()
    myStack.push(1, 1)
    myStack.push(11, 1)
    myStack.push(2, 2)
    myStack.print_stack()
    myStack.push(3, 3)
    myStack.push(22, 2)
    myStack.push(111, 1)
    myStack.push(333, 3)
    myStack.print_stack()
    print(myStack.pop(1))
    print(myStack.pop(1))
    myStack.print_stack()
    print(myStack.pop(2))
    myStack.print_stack()
    print(myStack.pop(1))
    print(myStack.pop(1))
    myStack.print_stack()
    myStack.push(22, 2)
    myStack.print_stack()
    myStack.push(222, 2)
    myStack.push(2222, 2)
    myStack.push(222.2, 2)
    myStack.push(222.2222, 2)
    myStack.print_stack()






    
        


