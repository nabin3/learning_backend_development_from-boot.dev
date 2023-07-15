'''
Some of our players have older computers, and they've noticed that our game is crashing because it requires too much memory. We've narrowed down the issue to the attack_action() function. Let's debug the function call stack and visualize which functions are being called from within.

Modify attack_action to call functions shoot_arrow and calc_new_health using call()
We have to make sure our shoot_arrow function is calculating the damage it will deal.

Modify shoot_arrow to call calc_damage using call()
Now that we know how much damage our arrow will do, we need to apply that damage to the target.

Modify calc_damage to call apply_damage using call()
'''

def attack_action():
    call(shoot_arrow)
    call(calc_new_health)

def shoot_arrow():
    call(calc_damage)

def calc_damage():
    call(apply_damage)

def calc_new_health():
    pass

def apply_damage():
    pass

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


stack = Stack()

def call(func):
    stack.push(func.__name__)
    print("pushing " + func.__name__)
    print("Stack: " + str(stack.items))
    print("=============================")
    func()
    stack.pop()
    print("popping " + func.__name__)
    print("Stack: " + str(stack.items))

call(attack_action)
