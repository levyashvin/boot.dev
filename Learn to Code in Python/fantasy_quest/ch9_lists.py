'''
Assignment L1

Let's work on Fantasy Quest's inventory! We can store items the player is carrying in a list!

Fix our get_inventory function by adding Shortsword to the end of the list.
'''

def get_inventory():
    return ["Healing Potion", "Leather Scraps", "Iron Helmet", "Shortsword"]


# Don't edit below this line


def test():
    inventory = get_inventory()
    print(f"Inventory contains: {inventory}")
    print("=====================================")


def main():
    test()


main()

'''
Assignment L5

We need to allow our players to access items in their inventories!

Fix our get_leather_scraps function by changing the value of item_index to the index in inventory that holds the value "Leather Scraps".
'''

def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]

    item_index = 1

    return inventory[item_index]

run_cases = [
    ("Leather Scraps",),
]

submit_cases = run_cases + [
    ("Leather Scraps",),
]


def test(expected_output):
    print("---------------------------------")
    print(f"Expecting: {expected_output}")
    result = get_leather_scraps()
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

'''
Assignment L6

Some of our player's inventories are huge, so looking through the entire list is cumbersome. Let's find an easy way for us to get the index of the last item in their inventory.

Complete the get_last_index function so that it returns the length of the inventory list minus 1.
'''

def get_last_index(inventory):
    return len(inventory) - 1

run_cases = [
    (["Potion"], 0),
    (["Potion", "Iron Breastplate"], 1),
    (["Potion", "Iron Breastplate", "Bread", "Longsword"], 3),
]

submit_cases = run_cases + [
    ([], -1),
    (["Single item"], 0),
    (["Shield", "Sword", "Bow", "Arrows", "Health Potion"], 4),
    (["Shield", "Sword", "Bow"], 2),
    (["Shield", "Sword"], 1),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_last_index(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

'''
Assignment L7

Fantasy Quest is trialing a new inventory system for their hardcore game mode. If a player has Iron Ore or an Iron Bar, it is always stored in the 2nd inventory slot (and they can only have one or the other).

Let's finish the smelt_ore function. When a player tries to smelt Iron Ore we need to change it into an Iron Bar, but only if they already have Iron Ore in their inventory slot.
'''

def smelt_ore(inventory):
    if inventory[1] == "Iron Ore":
        inventory[1] = "Iron Bar"
    return inventory

run_cases = [
    (
        ["Potion", "Iron Bar", "Iron Sword", "Leather Armor"],
        ["Potion", "Iron Bar", "Iron Sword", "Leather Armor"],
    ),
    ([None, None, None, None], [None, None, None, None]),
    (["Potion", "Iron Ore", None, None], ["Potion", "Iron Bar", None, None]),
]

submit_cases = run_cases + [
    (
        [None, "Iron Ore", None, "Leather Armor"],
        [None, "Iron Bar", None, "Leather Armor"],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = smelt_ore(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

'''
Assignment L8

We need to generate a unique user ID for each player in the game. An ID is just a unique number that identifies a user.

Let's finish the generate_user_list function. In the body of the loop, use the incrementing value i as unique IDs and append them to the player_ids list.

'''

def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)

    return player_ids

run_cases = [
    (5, list(range(5))),
    (10, list(range(10))),
]

submit_cases = run_cases + [
    (0, []),
    (1, [0]),
    (100, list(range(100))),
    (25, list(range(25))),
    (50, list(range(50))),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = generate_user_list(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

'''
Assignment

Our player is selling the items in their inventory to the shopkeep!

Pop the last element from the inventory list until there is nothing left. Pop the elements into an item variable so that each prints in turn on line 19.
'''

def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    # don't touch above this line

    for i in range(0, len(inventory)):
        item = inventory.pop()

        # don't touch below this line
        print(f"Selling: {item}")
        print(f"inventory: {inventory}")


def test():
    clear_inventory()
    print("=====================================")


def main():
    test()


main()

'''
Assignment L10

Our players need a way to see how many copies of a specific item they have within their inventory!

Let's finish the get_item_counts function. Within the loop, check if the items are a Potion, Bread, or Shortsword, then add up how many there are of each by incrementing the potion_count, bread_count and shortsword_count variables respectively.
'''

def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

    for i in range(0, len(items)):
        if items[i] == "Potion":
            potion_count += 1
        elif items[i] == "Bread":
            bread_count += 1
        elif items[i] == "Shortsword":
            shortsword_count += 1

    # don't touch below this line

    return potion_count, bread_count, shortsword_count

run_cases = [
    (["Bread", "Potion", "Shortsword", "Bread"], (1, 2, 1)),
    (["Potion", "Potion", "Shortsword", "Buckler", "Iron Mace"], (2, 0, 1)),
]

submit_cases = run_cases + [
    ([], (0, 0, 0)),
    (
        [
            "Potion",
            "Leather Scraps",
            "Bread",
            "Iron Ore",
            "Light Leather",
            "Bread",
            "Shortsword",
            "Longsword",
            "Ironwood Branch",
            "Shortsword",
            "Shortsword",
        ],
        (1, 2, 3),
    ),
    (["Bread", "Bread", "Bread", "Bread"], (0, 4, 0)),
    (["Shortsword", "Shortsword", "Shortsword", "Shortsword"], (0, 0, 4)),
    (["Potion"], (1, 0, 0)),
    (["Potion", "Bread", "Shortsword"], (1, 1, 1)),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input}")
    print(f"Expecting: {expected_output}")
    result = get_item_counts(input)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

'''
Assignment L13

We need to check if a player has a specific item in their inventory. In the contains_leather_scraps function, use the no-index syntax to iterate over each item in items. If you find an item called Leather Scraps, set the found variable to True.
'''

def contains_leather_scraps(items):
    found = False

    # don't touch above this line

    for item in items:
        if item == "Leather Scraps":
            found = True

    # don't touch below this line

    return found

run_cases = [
    (["Potion", "Healing Potion", "Iron Breastplate", "Leather Scraps"], True),
    (["Potion", "Shortsword", "Buckler", "Iron Mace"], False),
]

submit_cases = run_cases + [
    ([], False),
    (["Leather Scraps"], True),
    (["Potion", "Leather Scraps", "Leather Scraps"], True),
    (["Potion", "Healing Potion"], False),
    (["Leather scraps"], False),
    (["Leather", "Scraps"], False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = contains_leather_scraps(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

'''
Assignment L14

We keep track of each character's level in a list. When someone levels up, we want to know about it so we can congratulate them! Your assignment is to compare the old_character_levels and new_character_levels lists and to print the index where a character's level increased.

The existing code in the loop you've been given loops over all of the indexes in old_character_levels. Because old_character_levels and new_character_levels are the same lengths, you can reuse i to index into both.

Fill in the loop with code that prints the indexes where the item in the first list is less than the item in the second list; we don't want to congratulate someone for staying the same level (or somehow leveling down). For example, if the lists are:

old_character_levels = [2, 5, 3, 7, 5]
new_character_levels = [2, 5, 19, 7, 8]

Then your code should print these indexes:

2
4


'''

def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    # don't touch above this line

    for i in range(0, len(old_character_levels)):
        if old_character_levels[i] != new_character_levels[i]:
            print(i)


# don't touch below this line


def test():
    print("Character level increased at indexes:")
    check_character_levels()
    print("=====================================")


def main():
    test()


main()
