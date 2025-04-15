'''
Assignment L1

Complete the number_sum function. It should add up all the numbers from 1 to n. For example:

    number_sum(5) -> 1+2+3+4+5 -> 15
    number_sum(3) -> 1+2+3 -> 6

'''

def number_sum(n):
    return sum(range(n+1))

run_cases = [
    (3, 6),
    (5, 15),
]

submit_cases = run_cases + [
    (1, 1),
    (18, 171),
    (0, 0),
    (227, 25878),
    (100, 5050),
    (500, 125250),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = number_sum(input1)
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
Assignment L2

Write a function called find_min() that finds the smallest number in a list. For example:

    find_min([1, 3, -1, 2]) -> -1
    find_min([18, 3, 7, 2]) -> 2

'''

def find_min(list1):
    return min(list1)

run_cases = [
    ([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7], -4),
    ([4, 3, 2, 1, 18, 1, 2, 3, 4, 5, 6, 7], 1),
]

submit_cases = run_cases + [
    ([43, 234, 65465, 234, 2343, 443, 2123, 8768], 43),
    ([0], 0),
    ([-1, -2, -3], -3),
    ([100, 200, 300], 100),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = find_min(input1)
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
Assignment L3

Complete the remove_nonints() function. It takes a list and returns a new list but with all the non-integer types removed.

new_list = remove_nonints(["1", 1, "3", "400", 4, 500])
print(new_list)
# [1, 4, 500]
'''
def try_int(x):
    try:
        if int(x) == x:
            return True
        else:
            return False
    except Exception as e:
        return False

def remove_nonints(list1):
    return [x for x in list1 if type(x) == int]

run_cases = [
    (["200", 300, 2, False, "otherstring", 6], [300, 2, 6]),
    ([True, 300, 2, False, "otherstring", 76, 86, "morestrings"], [300, 2, 76, 86]),
]

submit_cases = run_cases + [
    ([300, 300, 2, False, "otherstring", 6, {}, 16], [300, 300, 2, 6, 16]),
    (["200", 300, 2, False, "something", 7, "something else"], [300, 2, 7]),
    (["string", True, {}, []], []),
    ([], []),
    ([123, 456, 789], [123, 456, 789]),
    (["123", "456", "789"], []),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print("")
    result = remove_nonints(input)
    print(f"Expecting: {expected_output}")
    print(f"Actual:    {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            print("Pass")
            passed += 1
        else:
            print("Fail")
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
Assignment L4

Complete the factorial() function. It should return the factorial of a given number.
'''

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

run_cases = [
    (0, 1),
    (4, 24),
]

submit_cases = run_cases + [
    (1, 1),
    (5, 120),
    (7, 5040),
    (9, 362880),
    (13, 6227020800),
    (15, 1307674368000),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print("")
    result = factorial(input)
    print(f"Expecting: {expected_output}")
    print(f"Actual:    {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            print("Pass")
            passed += 1
        else:
            print("Fail")
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

Complete the area_sum() function. It accepts a list of rectangles, where each rectangle is a dictionary that has the following structure:

{
  "height": 5,
  "width": 6
}

It should calculate the area of each rectangle and return the sum of all the areas.
'''

def area_sum(rectangles):
    return sum([x["height"] * x["width"] for x in rectangles])

run_cases = [
    ([{"height": 4, "width": 5}], 20),
    ([{"height": 4, "width": 5}, {"height": 4, "width": 9}], 56),
    ([{"height": 4, "width": 5}, {"height": 18, "width": 5}], 110),
]

submit_cases = run_cases + [
    ([{"height": 2, "width": 3}, {"height": 4, "width": 5}], 26),
    ([{"height": 6, "width": 7}, {"height": 8, "width": 9}], 114),
    ([{"height": 10, "width": 11}, {"height": 12, "width": 13}], 266),
    ([{"height": 0, "width": 0}], 0),
    ([], 0),
]


def test(input1, expected_output):
    print("---------------------------------")
    print("Input:")
    for rect in input1:
        print(f" - {rect}")
    print("")
    result = area_sum(input1)
    print(f"Expecting: {expected_output}")
    print(f"Actual:    {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            print("Pass")
            passed += 1
        else:
            print("Fail")
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

Complete the divide_list() function. It takes a list and a number as input, and should return a new list that contains all the elements of the original list after dividing them by the second input.

For example:

divided_list = divide_list([6, 8, 10], 2)
print(divided_list)
# [3.0, 4.0, 5.0]

'''

def divide_list(nums, divisor):
    return [x/divisor for x in nums]

run_cases = [
    ([6, 8, 10], 2, [3.0, 4.0, 5.0]),
    ([1, 2, 3, 4], 1, [1.0, 2.0, 3.0, 4.0]),
]

submit_cases = run_cases + [
    ([15, 30, 45], 3, [5.0, 10.0, 15.0]),
    ([0], 1, [0.0]),
    ([27, 54, 81], 9, [3.0, 6.0, 9.0]),
    ([100, 200, 300, 400], 10, [10.0, 20.0, 30.0, 40.0]),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * List of numbers: {input1}")
    print(f" * Divisor: {input2}")
    print(f"Expecting: {expected_output}")
    result = divide_list(input1, input2)
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

Complete the join_strings() function. It takes a list of strings and returns a new single string. The new string is the concatenation of all the input strings from the list end-to-end, in order, with a comma between them.

For example:

string_list = ["Annie", "Reiner", "Bertholdt"]
joined_string = join_strings(string_list)
print(joined_string)
# "Annie,Reiner,Bertholdt"

string_list = ["Eren", "Mikasa", "Armin"]
joined_string = join_strings(string_list)
print(joined_string)
# "Eren,Mikasa,Armin"
'''

def join_strings(strings):
    joined = ""
    for string in strings:
        joined += "," + string
    return joined[1:]

run_cases = [
    (["hello", "world"], "hello,world"),
    (["this", "list", "is", "so", "important"], "this,list,is,so,important"),
]

submit_cases = run_cases + [
    ([], ""),
    (["zuck", "satya", "cook", "bezos"], "zuck,satya,cook,bezos"),
    (["dota", "sc2", "overwatch", "diablo", "mtg"], "dota,sc2,overwatch,diablo,mtg"),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print("")
    result = join_strings(input1)
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
