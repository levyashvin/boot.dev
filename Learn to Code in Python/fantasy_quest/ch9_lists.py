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
Assignment L2

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

'''