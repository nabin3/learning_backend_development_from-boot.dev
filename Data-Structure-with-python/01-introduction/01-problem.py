''' Implement the count_potions function. It should take a list of our players' inventory (strings) as input and return the number of times Healing potion shows up in the list as an integer.

For example

count = count_potions(['Short sword', 'Bread', 'Healing potion', 'Healing potion'])
print(count)
# prints "2"
'''

import random

def count_potions(inventory):
    count = 0
    for item in inventory:
        if item == "Healing potion":
            count += 1
    return count

def get_inventory(num):
    random.seed(1)
    options = [
        "Short sword",
        "Bread",
        "Healing potion",
        "Leather scraps",
        "Chainmail Armor",
    ]
    inventory = []
    for i in range(num):
        optionI = random.randint(0, len(options) - 1)
        inventory.append(options[optionI])
    return inventory

        
def test(num):
    inventory = get_inventory(num)
    print(f"Total items in inventory: {num}")
    print(f"number of potions in inventory: {count_potions(inventory)}")
    print("====================================")


def main():
    test(10)
    test(100)
    test(1000)
    test(10000)

main()
