'''
Assignment L1

Complete the missing sections of the calculate_damage function.

    Fix the total_damage variable so that it contains the sum of all the different weapons' and spells' damage values.
    Fix the average_damage variable so that it contains the average of the combined weapon and spell damage.

'''

def calculate_damage(*weapons):
    total_damage = sum(weapons)
    average_damage = total_damage / len(weapons)
    return total_damage, average_damage

run_cases = [
    (3, 5, 2, 1, 4, (15, 3.0)),
    (5, 5, 5, 5, 5, (25, 5.0)),
]

submit_cases = run_cases + [
    (1, 2, 3, 4, 5, (15, 3.0)),
    (0, 0, 0, 0, 10, (10, 2.0)),
    (0, 0, 0, 0, 0, (0, 0.0)),
    (10, 20, 30, 40, 50, (150, 30.0)),
    (2, 2, 2, 2, 2, (10, 2.0)),
    (1, 1, 1, 1, 1, (5, 1.0)),
]


def test(sword, arrow, spear, dagger, fireball, expected_output):
    print("---------------------------------")
    print(f"Inputs: {sword}, {arrow}, {spear}, {dagger}, {fireball}")
    print(f"Expecting: {expected_output}")
    result = calculate_damage(sword, arrow, spear, dagger, fireball)
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
Assignment L5

Complete the update_player_score function. It should add increment to current_score and then return the new current_score.
'''

def update_player_score(current_score, increment):
    return current_score + increment

run_cases = [
    (0, 100, 100),
    (100, 200, 300),
]

submit_cases = run_cases + [
    (300, 300, 600),
    (600, 50, 650),
    (0, 0, 0),
    (1, 1, 2),
    (100, -50, 50),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = update_player_score(input1, input2)
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

Complete the get_hurt function. It should use the -= in-place operator to subtract damage from current_health and then return the new current_health.
'''

def get_hurt(current_health, damage):
    current_health -= damage
    return current_health

run_cases = [
    (1000, 100, 900),
    (900, 60, 840),
]

submit_cases = run_cases + [
    (840, 10, 830),
    (830, 3, 827),
    (0, 0, 0),
    (1, 1, 0),
    (100, 2, 98),
    (2500, 3, 2497),
]


def test(current_health, damage, expected_output):
    print("---------------------------------")
    print(f"Inputs: {current_health}, {damage}")
    print(f"Expecting: {expected_output}")
    result = get_hurt(current_health, damage)
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

Due to the constraints of our app's server, there is a maximum number of players we can have on a single Fantasy Quest server.

Complete the max_players_on_server function. It takes no inputs, but simply returns 3 static numbers:

    The max players on a "small" server: 1,024,000,000,000,000,000 (1.024e18)
    The max players on a "medium" server: 10,240,000,000,000,000,000
    The max players on a "large" server: 102,400,000,000,000,000,000

Use scientific notation to represent these numbers. For example: 3.104e15.
'''

def max_players_on_server():
    return 1.024e18, 10.24e18, 102.4e18

run_cases = [
    (1.024e18, 1.024e19, 1.024e20),
]

submit_cases = run_cases


def test(expected1, expected2, expected3):
    print("---------------------------------")
    print(f"Expecting: {(expected1, expected2, expected3)}")
    result = max_players_on_server()
    print(f"Actual: {result}")
    if result == (expected1, expected2, expected3):
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
Assignment L15

Complete each of the get_XXX_bits functions. Simply use the bitwise & operation on the input of the user's permission bits and the appropriate guild permission bits variable, and return the resulting bits for them to be checked by the tests.

4 values have been provided, use the appropriate one for each function:

    can_create_guild
    can_review_guild
    can_delete_guild
    can_edit_guild

'''

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    return user_permissions & can_create_guild


def get_review_bits(user_permissions):
    return user_permissions & can_review_guild


def get_delete_bits(user_permissions):
    return user_permissions & can_delete_guild


def get_edit_bits(user_permissions):
    return user_permissions & can_edit_guild

run_cases = [
    (0b0110, False, True, True, False),
    (0b1111, True, True, True, True),
    (0b0000, False, False, False, False),
]

submit_cases = run_cases + [
    (0b1001, True, False, False, True),
    (0b1000, True, False, False, False),
    (0b0100, False, True, False, False),
    (0b0010, False, False, True, False),
    (0b0001, False, False, False, True),
]


def test(
    input1, expected_output1, expected_output2, expected_output3, expected_output4
):
    print("---------------------------------")
    print(f"Inputs: {input1:04b}")
    print(f"Expecting can_create: {expected_output1}")
    print(f"Expecting can_review: {expected_output2}")
    print(f"Expecting can_delete: {expected_output3}")
    print(f"Expecting can_edit: {expected_output4}")

    result1 = get_create_bits(input1) == can_create_guild
    result2 = get_review_bits(input1) == can_review_guild
    result3 = get_delete_bits(input1) == can_delete_guild
    result4 = get_edit_bits(input1) == can_edit_guild

    print(f"Actual can_create: {result1}")
    print(f"Actual can_review: {result2}")
    print(f"Actual can_delete: {result3}")
    print(f"Actual can_edit: {result4}")
    if (
        result1 == expected_output1
        and result2 == expected_output2
        and result3 == expected_output3
        and result4 == expected_output4
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

'''
Assignment L14

Complete the calculate_guild_perms function. It takes as input four binary numbers representing the separate permissions of each member of the guild: glorfindel, galadriel, elendil and elrond. It should return a single binary number that represents the combined permissions of all the members of the guild.

Use a series of bitwise "or" operations to calculate the superset of all the member's permissions.
'''

def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    return glorfindel | galadriel | elendil | elrond

run_cases = [
    (0b0001, 0b0010, 0b0001, 0b1011, 0b1011),
]

submit_cases = run_cases + [
    (0b0000, 0b0000, 0b0000, 0b1011, 0b1011),
    (0b1001, 0b0010, 0b1101, 0b1011, 0b1111),
]


def test(input1, input2, input3, input4, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
    print(f"Expecting: {expected_output}")
    result = calculate_guild_perms(input1, input2, input3, input4)
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
Assignment C1

Fix the intern's syntax error. The calculate_dps function takes two inputs, but due to the syntax error, it's taking in 4 instead. Use the proper delimiter so that the numbers are still easy to parse visually.

The two input numbers should be:

    damage: 8 million, time: 45
    damage: 10 million, time: 49

'''

def main():
    calculate_dps(8e6, 45)
    calculate_dps(10e6, 49)


# Don't edit below this line


def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")


main()

'''
Assignment C2

Complete the binary_string_to_int function. It takes three binary strings as input and returns each of them in the same order as integers. Each integer is the numerical value of the string when interpreted as binary.
'''

def binary_string_to_int(num_servers, num_players, num_admins):
    return int(num_servers, 2), int(num_players, 2), int(num_admins, 2)

run_cases = [
    ("1", "10", "1010", (1, 2, 10)),
    ("101", "11", "10100", (5, 3, 20)),
    ("111", "1011", "11010", (7, 11, 26)),
]

submit_cases = run_cases + [
    ("0", "0", "0", (0, 0, 0)),
    ("1111", "1111", "1111", (15, 15, 15)),
    ("101010", "110011", "101010", (42, 51, 42)),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    print(f"Expecting: {expected_output}")
    result = binary_string_to_int(input1, input2, input3)
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