'''
Assignment L1

One of the calls to get_player_record is throwing a player id not found exception. Change the code in the main function to safely make all four calls within one try-except block. If an exception is raised, print the exception instead.
'''

def main():
    try:
        print(get_player_record(1))
        print(get_player_record(2))
        print(get_player_record(3))
        print(get_player_record(4))
    except Exception as e:
        print(e)


# Don't edit below this line


def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")


main()

'''
Assignment

If a player_id that doesn't exist is passed into the get_player_record function, we need to raise (but not handle) our own error to alert the caller of our function that the player they are looking for doesn't exist. The exception should say player id not found.
'''

def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    else:
        raise Exception("player id not found")

run_cases = [
    (1, {"name": "Slayer", "level": 128}),
    (4, Exception("player id not found")),
    (3, {"name": "Saruman", "level": 4000}),
]

submit_cases = run_cases + [
    (2, {"name": "Dorgoth", "level": 300}),
    (5, Exception("player id not found")),
    (0, Exception("player id not found")),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * player_id: {input1}")
    print(f"Expecting: {expected_output}")
    try:
        result = get_player_record(input1)
        print(f"Actual: {result}")
        if isinstance(expected_output, Exception):
            print("Fail -- expected exception")
            return False
        if result == expected_output:
            print("Pass")
            return True
    except Exception as e:
        print(f"Actual: {e}")
        if isinstance(expected_output, Exception) and str(e) == str(expected_output):
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

Take a look at the get_player_record function. It raises an exception for negative player_ids.

Complete the process_player_record() function. Pass player_id to get_player_record and return the result, but if an IndexError is raised, instead return the string: index is too high. Otherwise, if any other exception is raised, return the error.
'''

def process_player_record(player_id):
    try:
        return get_player_record(player_id)
    except IndexError:
        print("inedx is too high")
    except Exception as e:
        print(e)


# Don't edit below this line


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]

'''
Assignment L11

Complete the purchase_item function.

    If the character doesn't have enough gold raise an Exception with the text not enough gold.
    Otherwise, return the amount of remaining money the customer has after completing the purchase.

'''

def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception("not enough gold")
    return gold_available - price

run_cases = [
    (10.00, 20.00, 10.00),
    (30.00, 20.00, None, "not enough gold"),
]

submit_cases = run_cases + [
    (15.10, 15.10, 0.00),
    (1430.00, 69.00, None, "not enough gold"),
    (7.50, 7.50, 0.00),
    (100.00, 99.99, None, "not enough gold"),
    (0.00, 0.00, 0.00),
]


def test(price, gold_available, expected_output, expected_err=None):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * price: {price:.2f}")
    print(f" * gold_available: {gold_available:.2f}")
    try:
        result = purchase_item(price, gold_available)
        if result == expected_output:
            print(f"Expected: {expected_output:.2f}")
            print(f"  Actual: {result:.2f}")
            print("Pass")
            return True
    except Exception as e:
        print(f"Expected Exception: {expected_err}")
        print(f"  Actual Exception: {str(e)}")
        if str(e) == expected_err:
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
