'''
    Our players need the option to find the last item in their inventory.

Implement the last_item function. It should take a list of our player's inventory (strings) and return the last element in the list.
'''

import random


def last_item(inventory):
    return inventory[len(inventory)-1]


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
    print(f"Total items in Inventory: {num}")
    print(f"Last item in Inventory: {last_item(inventory)}")
    print("=================================")


def main():
    test(10)
    test(100)
    test(1000)
    test(10000)
    test(100000)


main()

