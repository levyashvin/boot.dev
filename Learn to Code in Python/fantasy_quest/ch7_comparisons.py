'''
Assignment L1

Complete the player_1_wins function. It should return True if player 1 has a higher score, and False otherwise.
'''

def player_1_wins(player_1_score, player_2_score):
    return player_1_score > player_2_score

run_cases = [
    (5, 6, False),
    (5, 5, False),
    (7, 6, True),
]

submit_cases = run_cases + [
    (10, 3, True),
    (2, 2, False),
    (0, 0, False),
    (10, 5, True),
    (5, 10, False),
]


def test(player_1_score, player_2_score, expected):
    print("---------------------------------")
    print(f"Inputs: {player_1_score}, {player_2_score}")
    print(f"Expecting: {expected}")
    result = player_1_wins(player_1_score, player_2_score)
    print(f"Actual: {result}")
    if result == expected:
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

Create the following variables. Use comparison operators to determine their boolean values. The context of the parameter names should tell you how to make these comparisons. Return them in this order:

    is_mustang_edward_same
    is_alphonse_edward_same
    is_winry_alphonse_same

'''

def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = edward_height == mustang_height
    is_alphonse_edward_same = alphonse_height == edward_height
    is_winry_alphonse_same = winry_height == alphonse_height
    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same

run_cases = [
    (5, 5, 7, 5, (True, True, False)),
    (6, 6, 5, 5, (False, True, False)),
]

submit_cases = run_cases + [
    (4, 4, 4, 4, (True, True, True)),
    (2, 2, 2, 2, (True, True, True)),
    (8, 8, 8, 7, (False, True, True)),
    (5, 7, 9, 11, (False, False, False)),
    (11, 9, 7, 5, (False, False, False)),
]


def test(elon, sara, jill, bob, expected):
    print("---------------------------------")
    print(f"Inputs: {elon}, {sara}, {jill}, {bob}")
    print(f"Expecting: {expected}")
    result = compare_heights(elon, sara, jill, bob)
    print(f"Actual: {result}")
    if result == expected:
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

Complete the can_withstand_blow function. It should return True if the hero's armor is greater than or equal to the damage dealt by the enemy, and False otherwise.
'''

def can_withstand_blow(hero_armor, enemy_damage):
    return hero_armor >= enemy_damage

run_cases = [(175, 250, False), (250, 175, True), (1, 1, True)]

submit_cases = run_cases + [(250, 250, True), (0, 0, True), (2, 3, False), (3, 2, True)]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = can_withstand_blow(input1, input2)
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
Assignment L4

Complete the print_status function.

    If player_health is less than or equal to 0, print the text dead to the console.
    Afterwards, whether or not the player is dead, print the text status check complete to the console.

'''

def print_status(player_health):
    if(player_health <= 0):
        print("dead")
    print("status check")


# Don't edit below this line


def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")


def main():
    test(0)
    test(5)
    test(-1)
    test(3)


main()

'''
Assignment L5

Complete the check_swords_for_army function. If the number of swords and the number of soldiers match, return the string:

correct amount

Otherwise, return the string:

incorrect amount

Punctuation matters! Make sure you return the strings exactly as they appear above.
'''

def check_swords_for_army(number_of_swords, number_of_soldiers):
    if(number_of_swords == number_of_soldiers):
        return "correct amount"
    else:
        return "incorrect amount"
    
run_cases = [
    (500, 1000, "incorrect amount"),
    (800, 800, "correct amount"),
]

submit_cases = run_cases + [
    (1500, 1000, "incorrect amount"),
    (200, 200, "correct amount"),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = check_swords_for_army(input1, input2)
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

Complete the player_status function. If the player's health is less than or equal to 0, return the string:

dead

Otherwise, if it's less than or equal to 5 return the string:

injured

Otherwise, return the string:

healthy

'''

def player_status(health):
    if(health <= 0):
        return "dead"
    elif(health <= 5):
        return "injured"
    else:
        return "healthy"
    
run_cases = [
    (0, "dead"),
    (4, "injured"),
]

submit_cases = run_cases + [
    (6, "healthy"),
    (5, "injured"),
    (1, "injured"),
    (10, "healthy"),
    (-1, "dead"),
]


def test(health, expected_status):
    print("---------------------------------")
    print(f"Health: {health}")
    print(f"Expecting: {expected_status}")
    result = player_status(health)
    print(f"Result: {result}")
    if result == expected_status:
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

There is a bug in the check_high_score function! Add the proper conditional statement to fix the bug. If the names match, return the string:

You are the highest scoring player!

Otherwise, return:

You are not the highest scoring player!

'''

def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"

run_cases = [
    ("ash ketchum", "ash ketchum", "You are the highest scoring player!"),
    ("brock", "ash ketchum", "You are not the highest scoring player!"),
]

submit_cases = run_cases + [
    ("misty", "brock", "You are not the highest scoring player!"),
    ("", "", "You are the highest scoring player!"),
    ("same", "same", "You are the highest scoring player!"),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = check_high_score(input1, input2)
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

Complete the check_high_score function. If the player_name matches the high score name, return the string:

high

Otherwise, if it's the low scorer, return the string:

low

Otherwise, return the string:

neither

'''

def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if(player_name == high_scoring_player_name):
        return "high"
    if(player_name == low_scoring_player_name):
        return "low"
    else:
        return "neither"
    
run_cases = [
    ("ash ketchum", "ash ketchum", "brock", "high"),
    ("brock", "ash ketchum", "brock", "low"),
]

submit_cases = run_cases + [
    ("misty", "brock", "ash ketchum", "neither"),
    ("red", "red", "blue", "high"),
    ("blue", "red", "blue", "low"),
    ("green", "red", "blue", "neither"),
]


def test(
    player_name, high_scoring_player_name, low_scoring_player_name, expected_output
):
    print("---------------------------------")
    print(
        f"Player Name: {player_name}, High Scoring Player: {high_scoring_player_name}, Low Scoring Player: {low_scoring_player_name}"
    )
    print(f"Expecting: {expected_output}")
    result = check_high_score(
        player_name, high_scoring_player_name, low_scoring_player_name
    )
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
Assignment L9

We need a way for our game to track whether a character's attack hits or misses.

Complete the does_attack_hit function. The function should return True if either of the following conditions are met:

    The attack_roll is not a 1 and the attack roll is greater than or equal to the armor_class, or
    The attack roll is a 20

Otherwise, it should return False.
'''

def does_attack_hit(attack_roll, armor_class):
    return (attack_roll != 1 and attack_roll >= armor_class) or (attack_roll == 20)

run_cases = [
    (17, 18, False),
    (20, 25, True),
]

submit_cases = run_cases + [
    (1, 0, False),
    (16, 13, True),
    (5, 5, True),
    (1, 1, False),
    (20, 20, True),
    (15, 10, True),
    (2, 3, False),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = does_attack_hit(input1, input2)
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
Assignment L11

In Fantasy Quest, players can go to a town's local pub. Drinking virtual beer refills their stamina!

Complete the function that determines if a bartender should serve drinks to a customer. Only return True if all of these conditions apply. If any of these conditions are False, return False:

    The customer's age is 21 or older
    The bartender is working
    The time is at least 5 but no later than 10

'''

def should_serve_customer(customer_age, on_break, time):
    return customer_age >= 21 and on_break == False and (time <= 10 and time >= 5)

run_cases = [
    (22, False, 10, True),
    (41, False, 1, False),
    (14, False, 7, False),
]

submit_cases = run_cases + [
    (21, False, 5, True),
    (107, False, 9, True),
    (23, True, 5, False),
    (21, False, 4, False),
    (57, False, 11, False),
    (20, False, 5, False),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * customer_age: {input1}")
    print(f" * on_break: {input2}")
    print(f" * time: {input3}")
    print(f"Expecting: {expected_output}")
    result = should_serve_customer(input1, input2, input3)
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
Assignment c1

Write the check_mount_rental function. It takes two inputs:

    time_used - the amount of time the mount has been used in minutes
    time_purchased - the amount of time the character rented the mount for

    If time_used meets or exceeds time_purchased, then the rental is expired and greedy Uper will charge a fee, so the function should return the string "overtime charged"
    Otherwise, return the string "no charges yet"

'''

def check_mount_rental(time_used, time_purchased):
    if(time_used >= time_purchased):
        return "overtime charged"
    return "no charges yet"

run_cases = [
    (3, 4, "no charges yet"),
    (5, 2, "overtime charged"),
]

submit_cases = run_cases + [
    (2, 2, "overtime charged"),
    (0, 1, "no charges yet"),
    (1, 1, "overtime charged"),
    (100, 2, "overtime charged"),
    (2500, 3, "overtime charged"),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = check_mount_rental(input1, input2)
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
Assignment C2

On line 4 write an if/elif/else block. Using the rules specified above, set advantage, disadvantage, or evenly_matched to True depending on the values of player_power and enemy_defense.

For example, if the player's power is greater than the enemy's defense, advantage should be set to True. etc.
'''

def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if(player_power > enemy_defense):
        advantage = True
    elif(player_power == enemy_defense):
        evenly_matched = True
    else:
        disadvantage = True

    return advantage, disadvantage, evenly_matched

run_cases = [
    (101, 100, True, False, False),
    (50, 100, False, True, False),
    (100, 100, False, False, True),
]

submit_cases = run_cases + [
    (150, 70, True, False, False),
    (80, 150, False, True, False),
    (0, 0, False, False, True),
    (1, 1, False, False, True),
    (1000, 500, True, False, False),
    (500, 1000, False, True, False),
]


def test(input1, input2, expected_output1, expected_output2, expected_output3):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output1}, {expected_output2}, {expected_output3}")
    result = combat_evaluation(input1, input2)
    print(f"Actual: {result}")
    if result == (expected_output1, expected_output2, expected_output3):
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
Assignment C3

Complete the has_enough_energy function to check if Tyler can make a round trip. The function takes 3 integers energy_available, distance_one_way, and meters_per_energy.

Do some Pythonic math with the distance_one_way and meters_per_energy variables to determine how many points of energy are needed for Tyler to get to the capital city AND make it back to the inn. Assign the result to a energy_needed variable. distance_one_way is how many meters it is to get from here to there. meters_per_energy is how far Tyler's rogue can travel with one energy point.

Return True if there is at least enough energy for a round trip both there and back based on the energy_needed variable, and False otherwise.
'''

def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    return energy_available * meters_per_energy >= 2 * distance_one_way

run_cases = [
    (8, 50, 22, True),
    (9, 100, 20, False),
]

submit_cases = run_cases + [
    (10, 50, 18, True),
    (3, 105, 22, False),
    (1, 1, 2, True),
    (2, 1, 1, True),
    (1, 2, 1, False),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    print(f"Expecting: {expected_output}")
    result = has_enough_energy(input1, input2, input3)
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
