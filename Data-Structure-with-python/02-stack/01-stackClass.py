'''Implement the following methods on the Stack class. Use

stack.push(item) -> Places a new item on top of the stack
stack.pop() -> Removes the top item from the stack and returns it. (return None if empty)
stack.peek() -> Returns the top item from the stack without modifying the stack. (return None if empty)
stack.size() -> Returns the number of items in the stack
'''
import random

class Stack:
    def __init__(self):
        self.arrows = []

    def push(self, arrow):
        self.arrows.append(arrow)

    def pop(self):
        if len(self.arrows) == 0:
            return None
        return self.arrows.pop()

    def peek(self):
        if len(self.arrows) == 0:
            return None
        return self.arrows[len(self.arrows) - 1]

    def size(self):
        return len(self.arrows)


def main():
    stack = Stack()
    fill_stack(stack, 2)
    size_stack(stack)
    pop_stack(stack)
    pop_stack(stack)

    fill_stack(stack, 6)
    peek_stack(stack)
    peek_stack(stack)
    size_stack(stack)
    pop_stack(stack)
    pop_stack(stack)
    pop_stack(stack)
    pop_stack(stack)
    pop_stack(stack)
    pop_stack(stack)

def pop_stack(stack):
    print("popping: " + str(stack.pop()))
    print(f"arrows: {stack.arrows}")
    print("======================================")
    return stack
    
def peek_stack(stack):
    print("peeking: " + str(stack.peek()))
    print(f"arrows: {stack.arrows}")
    print("======================================")
    return stack
 
def size_stack(stack):
    print("arrows size" + str(stack.size()))
    print("=======================================")
    return stack

def push_stack(stack, val):
    print("pushing" + str(val))
    stack.push(val)
    print(f"arrows: {stack.arrows}")
    print("=======================================")
    return stack

def fill_stack(stack, num):
    random.seed(1)
    options = ["Arrow", "Fire arrow", "Ice arrow", "Oil arrow", "Lightning Arrow"]
    for i in range(num):
        optionI = random.randint(0, len(options) - 1)
        push_stack(stack, options[optionI])
    return stack

main()
