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

'''
Assignment L15

Our players want a way to see their strongest attack from their last combat. Let's add another function to analyze data from our combat log.

Complete the find_max function that looks at each number in the nums list and returns the maximum value. If no maximum is found, it just returns negative infinity. I've added it for you as the starting value of max_so_far.
'''

def find_max(nums):
    max_so_far = float("-inf")
    for i in nums:
        if i > max_so_far:
            i=max_so_far = i
    return max_so_far

run_cases = [([1, 2, 3, 4, 5], 5), ([1, 2, 300, 4, 5], 300)]

submit_cases = run_cases + [
    ([1, 20, 3, 4, 5], 20),
    ([-1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 21, 18], 21),
    ([], float("-inf")),
    ([-1, -2, -3, -4, -5], -1),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = find_max(input1)
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
Assignment L16

Inside the loop in the get_odd_numbers function, use the modulo operator to check if each number, i, is odd. If a number is odd, append it to the odd_numbers list. The function already returns the odd_numbers list for you. num is an integer.
'''

def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        if i % 2 == 1:
            odd_numbers.append(i)

    # don't touch below this line

    return odd_numbers

run_cases = [(10, [1, 3, 5, 7, 9]), (20, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])]

submit_cases = run_cases + [
    (0, []),
    (1, []),
    (2, [1]),
    (300, [i for i in range(1, 300, 2)]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_odd_numbers(input1)
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
Assignment L17

Complete the given get_champion_slices function. It takes a list of champions and should return three new lists based on the given champions:

    First, return a slice of the champions list that starts with the third champion and goes to the end of the list.
    Next, return a slice of the champions list that starts at the beginning of the list and includes all champions except for the very last champion.
    Last, return a slice of the champions list that only includes the champions in even numbered indexes.

'''

def get_champion_slices(champions):
    return champions[2:], champions[:-1], champions[::1]

run_cases = [
    (
        ["Thrundar", "Morgate", "Gandolfo", "Thraine", "Norwad", "Gilforn"],
        (
            ["Gandolfo", "Thraine", "Norwad", "Gilforn"],
            ["Thrundar", "Morgate", "Gandolfo", "Thraine", "Norwad"],
            ["Thrundar", "Gandolfo", "Norwad"],
        ),
    ),
    (
        ["Frank", "Dennis", "Sweet Dee", "Mac", "Charlie"],
        (
            ["Sweet Dee", "Mac", "Charlie"],
            ["Frank", "Dennis", "Sweet Dee", "Mac"],
            ["Frank", "Sweet Dee", "Charlie"],
        ),
    ),
]

submit_cases = run_cases + [
    (([]), ([], [], [])),
    (
        (["John", "Sydney", "Spencer", "Bill", "Matthew", "Brandon", "Tony"]),
        (
            ["Spencer", "Bill", "Matthew", "Brandon", "Tony"],
            ["John", "Sydney", "Spencer", "Bill", "Matthew", "Brandon"],
            ["John", "Spencer", "Matthew", "Tony"],
        ),
    ),
]


def test(input1, expected_output):
    print("-" * 40)
    print(f"Input:\n{input1}")
    print(f"Expecting:\n{expected_output}")
    try:
        slice_1, slice_2, slice_3 = get_champion_slices(input1)
        result = (slice_1, slice_2, slice_3)
    except Exception as e:
        print(f"Error: {e}")
        return False
    print(f"Actual:\n{result}")
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
Assignment L18

Fantasy Quest allows users to keep lists of their favorite items. Your job is to finish the concatenate_favorites function. It takes three different lists - the player's favorite_weapons, favorite_armor and favorite_items.

    Create a new list that combines the lists favorite_weapons, favorite_armor, and favorite_items in this order.
    Return the list containing the combined favorites.

'''

def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    return favorite_weapons + favorite_armor + favorite_items

run_cases = [
    (
        ["sword", "dagger"],
        ["bracers", "helmet"],
        ["feather", "iron bars"],
        (["sword", "dagger", "bracers", "helmet", "feather", "iron bars"]),
    ),
]

submit_cases = run_cases + [
    (
        ["lance"],
        ["shield"],
        ["potions"],
        (["lance", "shield", "potions"]),
    ),
    (
        ["bow", "staff"],
        ["breastplate"],
        ["scrolls", "bedroll"],
        (["bow", "staff", "breastplate", "scrolls", "bedroll"]),
    ),
    ([], [], [], ([])),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    print(f"Expecting: {expected_output}")
    result = concatenate_favorites(input1, input2, input3)
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
Assignment L19

Our players have requested an in-game feature that will allow them to type in a weapon name to check if it's in the list of top weapons in the realm.

Complete the is_top_weapon function. It should return True if the weapon is in the top_weapons list, otherwise it should return False.

'''

def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]

    # don't touch above this line

    return weapon in top_weapons

run_cases = [
    ("sword of justice", True),
    ("bronze mace", False),
    ("sword of slashing", True),
]

submit_cases = run_cases + [
    ("", False),
    ("great axe", True),
    ("silver bow", True),
    ("golden spear", False),
    ("spiked knuckles", True),
    ("spellbook", True),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input:")
    print(f" * Weapon: {input1}")
    print(f"Expecting: {expected_output}")
    result = is_top_weapon(input1)
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
Assignment L20

In Fantasy Quest there is a list of strongholds on the map that players can visit to defeat powerful bosses. Let's update the trim_strongholds function to:

    Delete the first stronghold from the list
    Delete the last two strongholds from the list

'''

def trim_strongholds(strongholds):
    del strongholds[0]
    del strongholds[-2:]
    return strongholds

run_cases = [
    (
        [
            "Rivendale",
            "The Morgoth Mountains",
            "The Lonely Island",
            "Mordia",
            "Mordane",
            "Gondolin",
        ],
        [
            "The Morgoth Mountains",
            "The Lonely Island",
            "Mordia",
        ],
    ),
]

submit_cases = run_cases + [
    (
        [
            "Pogsmeade",
            "Dogwarts",
            "The Leaky Pot",
            "The Screaming Hut",
        ],
        [
            "Dogwarts",
        ],
    ),
    (
        [
            "Midgard",
            "Cosmo Canyon",
            "Nibelheim",
            "Costa del Sol",
            "Pallet Town",
            "Viridian City",
            "Salamandastron",
            "Redwall Abbey",
            "Fisherman's Horizon",
            "Waterdeep",
            "Elturel",
            "Candlekeep",
            "Chult",
            "Eorzea",
            "Ratchet",
            "Orgrimmar",
            "Stormwind",
            "Shattrath",
            "Dalaran",
        ],
        [
            "Cosmo Canyon",
            "Nibelheim",
            "Costa del Sol",
            "Pallet Town",
            "Viridian City",
            "Salamandastron",
            "Redwall Abbey",
            "Fisherman's Horizon",
            "Waterdeep",
            "Elturel",
            "Candlekeep",
            "Chult",
            "Eorzea",
            "Ratchet",
            "Orgrimmar",
            "Stormwind",
        ],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"    Input: {input1}")
    print(f"Expecting: {expected_output}")
    trim_strongholds(input1)
    print(f"   Actual: {input1}")
    if input1 == expected_output:
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
Assignment L21

The Fantasy Quest character system needs a list of "heroes" to be able to run the game properly. Someone wrote some pretty nasty code, and the code in question creates a heroes list where every 3rd index defines a new hero. First their name, then their age, then whether or not they're an "elf".

Fix the structure of the heroes list by changing it into a list of tuples, where each tuple represents one hero and contains their data in the same order.
'''

def get_heroes():
    heroes = [
        ("Glorfindel",
        2093,
        True),
        ("Gandalf",
        1054,
        False),
        ("Gimli",
        389,
        False),
        ("Aragorn",
        87,
        False),
    ]

    return heroes

run_cases = [
    (
        [
            (
                "Glorfindel",
                2093,
                True,
            ),
            (
                "Gandalf",
                1054,
                False,
            ),
            (
                "Gimli",
                389,
                False,
            ),
            (
                "Aragorn",
                87,
                False,
            ),
        ]
    ),
]

submit_cases = run_cases


def test(expected_output):
    print("---------------------------------")
    passed = True
    result = get_heroes()
    if not isinstance(result, list):
        print("Expected result to be a list")
        return False

    for i, hero in enumerate(expected_output):
        print(f"Expected: {hero} at index {i}")
        if i >= len(result):
            print(f"Actual: None at index {i}")
            print("Fail")
            passed = False
            continue
        print(f"Actual: {result[i]} at index {i}")
        if hero != result[i]:
            print("Fail")
            passed = False
        else:
            print("Pass")
    return passed


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(test_case)
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
Assignment L22

Let's add another function to our inventory system. Write a function that returns the first element from a list. If the list is empty then return the string ERROR instead.

'''

def get_first_item(items):
    if len(items) == 0:
        return "ERROR"
    return items[0]

run_cases = [
    ([1, 2], 1),
    (["Healing Potion"], "Healing Potion"),
    ([], "ERROR"),
]

submit_cases = run_cases + [
    (["Iron Ore", "Iron Bar", "Scimitar"], "Iron Ore"),
    (["Apple", "Banana", "Cherry"], "Apple"),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]),
    ([False, True, False], False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_first_item(input1)
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
Assignment L23

Some of our players would like to view their inventories in reverse order.

Let's write a function that takes a list as an input and returns a new list except all the items are in reverse order.

For example:

[1, 2, 3] -> [3, 2, 1]
['a', 'b', 'c', 'd'] -> ['d', 'c', 'b', 'a']

'''

def reverse_list(items):
    return items[::-1]

run_cases = [
    (
        ["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"],
        ["Kite Shield", "Iron Breastplate", "Healing Potion", "Shortsword"],
    ),
    ([1, 2, 300, 4, 5], [5, 4, 300, 2, 1]),
]

submit_cases = run_cases + [
    ([], []),
    (["a"], ["a"]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    (
        ["apple", "banana", "cherry", "date", "elderberry"],
        ["elderberry", "date", "cherry", "banana", "apple"],
    ),
    (["hello", "world"], ["world", "hello"]),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input list: {input}")
    print(f"Expected reversed list: {expected_output}")
    result = reverse_list(input)
    print(f"Actual reversed list: {result}")
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
Assignment L24

We need to filter the profanity out of our game's live chat feature! Complete the filter_messages function. It takes a list of chat messages as input and returns 2 new lists:

    A list of the same messages but with all instances of the word dang removed.
    A list containing the number of dang words that were removed from the message at that particular index.

Here are some examples:

messages = ["dang it bobby!", "look at it go"]
filter_messages(messages) # returns ["it bobby!", "look at it go"], [1, 0]

messages2 = ["That's the bloody dang Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a dang razor!"]
filter_messages(messages2) # returns ["That's the bloody Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a razor!"], [1, 0, 1]
'''

def filter_messages(messages):
    cleaned = []
    count = []
    for i in messages:
        count.append(i.count("dang"))
        cleaned_message = i.replace("dang ", "")
        cleaned_message = cleaned_message.replace(" dang", "")
        cleaned.append(cleaned_message)
    return cleaned, count

run_cases = [
    (
        ["darn it", "this dang thing won't work", "lets fight one on one"],
        ["darn it", "this thing won't work", "lets fight one on one"],
        [0, 1, 0],
    ),
]

submit_cases = run_cases + [
    (
        [
            "well dang it",
            "dang the whole dang thing",
            "kill that knight, dang it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the dang baddies",
        ],
        [
            "well it",
            "the whole thing",
            "kill that knight, it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the baddies",
        ],
        [1, 2, 1, 0, 0, 0, 1],
    ),
]


def test(input, expected_output1, expected_output2):
    print("---------------------------------")
    print(f"Input:")
    print(f" * messages: {input}")
    print("Expecting:")
    print(f" * filtered messages: {expected_output1}")
    print(f" * words removed: {expected_output2}")
    print("Actual:")
    try:
        result = filter_messages(input)
        print(f" * filtered messages: {result[0]}")
        print(f" * words removed: {result[1]}")
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False

    if result == (expected_output1, expected_output2):
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
Assignment L25

Complete the split_players_into_teams function.

It accepts a list of players (strings representing their names) and returns two lists in this order:

    A new list of all the players with even-numbered indexes in the original list.
    A new list of all the players with odd-numbered indexes in the original list.

Use a slice with a "step" to create two new lists from the players list. Don't be afraid to consult your spellbook for list slicing help!
'''

def split_players_into_teams(players):
    even_list = players[0::2]
    odd_list = players[1::2]
    return even_list, odd_list

run_cases = [
    (
        [
            "Harry",
            "Hermione",
            "Ron",
            "Ginny",
            "Fred",
            "Neville",
            "Draco",
            "Luna",
            "Cho",
            "Gregory",
            "Lee",
            "Michael",
            "Lavender",
            "Frank",
            "Anthony",
            "Allan",
        ],
        (
            ["Harry", "Ron", "Fred", "Draco", "Cho", "Lee", "Lavender", "Anthony"],
            [
                "Hermione",
                "Ginny",
                "Neville",
                "Luna",
                "Gregory",
                "Michael",
                "Frank",
                "Allan",
            ],
        ),
    ),
    (["Mike", "Walter", "Skyler", "Tuco"], (["Mike", "Skyler"], ["Walter", "Tuco"])),
]

submit_cases = run_cases + [
    (["Alice", "Bob", "Charlie", "David"], (["Alice", "Charlie"], ["Bob", "David"])),
    ([], ([], [])),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = split_players_into_teams(input1)
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

Complete the check_ingredient_match function. It accepts two lists of strings:

    recipe: The list of ingredients needed.
    ingredients: The list of ingredients the character has.

It should return two values:

    A float representing the percentage of required ingredients the character has.
    A new list of ingredients the character is missing but that are required.

For example, if these were the lists:

recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
ingredients = ["Dragon Scale", "Phoenix Feather", "Troll Tusk"]

percentage, missing_ingredients = check_ingredient_match(recipe, ingredients)
print(percentage, missing_ingredients)
# Prints: 75.00 ["Unicorn Hair"]
'''

def check_ingredient_match(recipe, ingredients):
    count = 0
    needs = []
    
    for i in recipe:
        if i in ingredients:
            count += 1
        else:
            needs.append(i)
            
    return count*100/len(recipe) , needs

run_cases = [
    (
        [
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        [
            "Elf Dust",
            "Goblin Ear",
        ],
        (50.0, ["Mandrake Root", "Griffin Feather"]),
    ),
    (
        [
            "Dragon Scale",
            "Unicorn Hair",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        [
            "Dragon Scale",
            "Phoenix Feather",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        (75.0, ["Unicorn Hair", "Troll Tusk"]),
    ),
]

submit_cases = run_cases + [
    (
        [
            "Dragon Scale",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
            "Unicorn Hair",
        ],
        [
            "Goblin Ear",
            "Elf Dust",
            "Griffin Feather",
            "Mermaid Tear",
            "Goblin Ear",
            "Phoenix Feather",
            "Troll Tusk",
            "Unicorn Hair",
        ],
        (
            75.0,
            [
                "Dragon Scale",
                "Mandrake Root",
            ],
        ),
    ),
    (
        [
            "Orc Tears",
            "Orge Ear",
            "Goblin Giggles",
            "Witch Broom",
            "Giant Toenail Clipping",
            "Centipede Foot",
            "Dog Hair",
            "Bald Eagle Dandruff",
        ],
        [
            "Unicorn Hair",
            "Dragon Scale",
            "Phoenix Feather",
            "Troll Tusk",
            "Griffin Feather",
            "Mandrake Root",
            "Goblin Ear",
            "Bald Eagle Dandruff",
        ],
        (
            12.5,
            [
                "Orc Tears",
                "Orge Ear",
                "Goblin Giggles",
                "Witch Broom",
                "Giant Toenail Clipping",
                "Centipede Foot",
                "Dog Hair",
            ],
        ),
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print("Inputs:")
    print(f" - Recipe: {input1}")
    print(f" - Ingredients: {input2}")
    print("")
    result = check_ingredient_match(input1, input2)
    print(f"Expecting: {expected_output}")
    print(f"Actual:    {result}")
    if result[0] == expected_output[0] and sorted(result[1]) == sorted(
        expected_output[1]
    ):
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