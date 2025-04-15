'''
Assignment L1

Complete the remove_duplicates function. It should take a list of spells that a player has learned and return a new List where there is at most one of each title. You can accomplish this in at least two ways:

Iteration:

    Create a set to track spells that have been seen
    Create a list to store the unique spells
    Iterate over the list
        If the spell is not in the set, add it to the set and the list
    Return the list

Set conversion:

    Convert the list to a set
    Convert the set back to a list and return it.

It makes no sense to learn a spell twice! Once it's learned, it's learned forever.
'''

def remove_duplicates(spells):
    return list(set(spells))

run_cases = [
    (
        [
            "fireball",
            "eldritch blast",
            "fireball",
            "eldritch blast",
            "chill touch",
            "eldritch blast",
            "chill touch",
            "chill touch",
            "fireball",
            "fireball",
            "shocking grasp",
            "fireball",
            "fireball",
        ],
        ["chill touch", "eldritch blast", "fireball", "shocking grasp"],
    )
]

submit_cases = run_cases + [
    (["fireball", "fireball", "fireball"], ["fireball"]),
    (
        ["fireball", "eldritch blast", "chill touch", "shocking grasp"],
        ["chill touch", "eldritch blast", "fireball", "shocking grasp"],
    ),
    (["chill touch", "chill touch", "chill touch"], ["chill touch"]),
    (["shocking grasp", "shocking grasp", "shocking grasp"], ["shocking grasp"]),
    ([], []),
    (["eldritch blast", "eldritch blast", "eldritch blast"], ["eldritch blast"]),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * spells: {input}")
    print(f"Expecting: {expected_output}")
    result = remove_duplicates(input)
    print(f"   Actual: {result}")
    if not isinstance(result, list):
        print("Fail: result is not a list")
        return False
    result.sort()
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
Assignment L5

Complete the count_vowels function. It takes a string and returns:

    The number of vowels in the string
    A set of the unique vowels found in the string

We are only interested in the 5 vowels: a, e, i, o, u, and their capitalized versions. Treat uppercase and lowercase vowels as separate. For example, "A" and "a" are not the same.
'''
from functools import reduce
def count_vowels(text):
    return reduce(lambda count, i: count+1 if i in "aeiouAEIOU" else count, text, 0), set([x for x in text if x in "aeiouAEIOU"])

run_cases = [
    (
        "Did someone say Thunderfury, Blessed Blade of the Windseeker?",
        (19, {"u", "o", "i", "e", "a"}),
    ),
    ("LF9M UBRS NEED ALL!!!!", (4, {"U", "E", "A"})),
]

submit_cases = run_cases + [
    ("Leatherworker LFW Have all end game recipes!", (14, {"e", "i", "o", "a"})),
    ("", (0, set())),
    (
        "Can anyone spare 1g so I can train my new spells?",
        (13, {"o", "I", "i", "e", "a"}),
    ),
    ("no", (1, {"o"})),
    ("mages need a nerf", (6, {"e", "a"})),
    ("wtb port to Roshar", (4, {"o", "a"})),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Text: {input1}")
    print(f"Expecting: {expected_output}")
    result = count_vowels(input1)
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

Complete the find_missing_ids function. It accepts two lists as input, and returns a new set of all the IDs that are in the first list but are not in the second.

Naturally, there will be no duplicates in the resulting set.
'''

def find_missing_ids(first_ids, second_ids):
    return set(first_ids) - set(second_ids)

run_cases = [
    ([1, 1, 1, 2, 2, 2, 3], [1, 2], {3}),
    ([1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10], [1, 2, 2, 3, 4, 5, 6, 7, 8], {9, 10}),
]

submit_cases = run_cases + [
    ([], [], set()),
    ([1, 1, 1], [], {1}),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], set()),
    ([1, 1, 2, 2, 3, 3], [1, 2, 3], set()),
    ([1, 2, 3, 4, 5], [1, 2, 3], {4, 5}),
    ([1, 2, 3, 4, 5], [1, 3, 5], {2, 4}),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print("Inputs:")
    print(f" - first_ids:  {input1}")
    print(f" - second_ids: {input2}")
    result = find_missing_ids(input1, input2)
    print(f"Expecting: {expected_output}")
    print(f"Actual:    {result}")
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
