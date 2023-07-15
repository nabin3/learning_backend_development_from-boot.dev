''' Write a function is_balanced(input_str) that takes a string input_str as input and returns True if the parentheses in the string are balanced, and False otherwise. Use a stack to keep track of the parentheses.

Note: You only need to consider the characters ( and ) for this challenge. '''
def is_balanced(input_str):
    '''
    stack = Stack()
    for ch in input_str:
        if ch == "(":
            stack.push(ch)
        elif ch == ")":
            if "(" == stack.peek():
                stack.pop()
            else:
                stack.push(ch)
    return stack.peek() == None
    '''
    #optimized
    stack = Stack()
    for ch in input_str:
        if ch == "(":
            stack.push(ch)
        elif stack.pop() == None:
            return False
    return stack.peek() == None


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]


def test(input_str):
    print(f"input: {input_str}")
    print(f"output: {is_balanced(input_str)}")
    print("=============================")


def main():
    test("(")
    test("()")
    test("(())")
    test("()()")
    test("(()))")
    test("((())())")
    

main()
