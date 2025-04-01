'''
Assignment L1

Complete the missing sections of the for-loop in the print_numbers function so that it prints the numbers 0-99 to the console.
'''

def print_numbers():
    for i in range(0, 100):
        print(i)


# Don't edit below this line


def test():
    print("Printing numbers from 0 to 99:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()

'''
Assignment L2

In the print_numbers function, write a for-loop from scratch that logs the numbers 0-199 to the console.
'''

def print_numbers():
    for i in range(0, 200):
        print(i)


# Don't edit below this line


def test():
    print("Printing numbers from 0 to 199:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()

'''
Assignment L3

In the print_numbers_from_five_to function, the for-loop starts at 0. It should start at 5. Only change the start.
'''

def print_numbers_from_five_to(end):
    for i in range(5, end):
        print(i)


# Don't edit below this line


def test(end):
    print(f"Using input end: {end}")
    print(f"Printing numbers from 5 to {end - 1}:")
    print_numbers_from_five_to(end)
    print("=====================================")


def main():
    test(16)
    test(6)
    test(11)


main()

'''
Assignment L7

Fix the for loop in the count_down function. It takes start and end inputs, but start is always greater than end. It's supposed to print numbers counting down from start to end, exclusive, but there's a mistake in the range function call.
'''

def count_down(start, end):
    for i in range(end, start):
        print(i)


# Don't edit below this line


def test(start, end):
    print(f"Using inputs start: {start} and end: {end}")
    print(f"Printing numbers from {start} to {end + 1}:")
    count_down(start, end)
    print("=====================================")


def main():
    test(10, 0)
    test(20, 10)
    test(15, 11)


main()

'''
Assignment

Fix the bug in the sum_of_numbers function. Instead of adding 1 to total at each iteration of the loop, it should add i. For example, instead of:

1 + 1 + 1 + 1 + 1...

we want:

0 + 1 + 2 + 3 + 4...

The desired output is a single number after the loop has finished executing.
'''

def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total

run_cases = [(0, 5, 10), (0, 10, 45), (10, 20, 145)]

submit_cases = run_cases + [
    (1, 100, 4950),
    (5, 50, 1215),
    (20, 30, 245),
    (50, 60, 545),
    (100, 110, 1045),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * start: {input1}")
    print(f" * end: {input2}")
    print(f"Expecting: {expected_output}")
    result = sum_of_numbers(input1, input2)
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

Complete the sum_of_odd_numbers function. It should calculate the sum of all the odd numbers starting at 1 up to (but not including) the given end number and return the result.
'''

def sum_of_odd_numbers(end):
    total = 0
    for i in range(0, end):
        if(i % 2 == 1):
            total += i
    return total

run_cases = [
    (4, 4),
    (6, 9),
]

submit_cases = run_cases + [
    (0, 0),
    (1, 0),
    (2, 1),
    (4, 4),
    (10, 25),
    (15, 49),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * end: {input1}")
    print(f"Expecting: {expected_output}")
    result = sum_of_odd_numbers(input1)
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
Assignment L10

In Fantasy Quest, player characters regenerate health when standing still while away from enemies. This means they will gain health but can't run from enemies that are coming towards them while regenerating.

Complete the regenerate function using a while loop. It takes current_health, max_health and enemy_distance integers.

    While regenerating health, a character first gains 1 health each iteration until it reaches the max_health amount.
    The enemy_distance then shortens by 2 for each iteration.
    If an enemy is at a distance of 3 or less from the character, the character is not able to regenerate health. (Flipping that, if an enemy is more than a distance of 3 from the character, then the character is able to regenerate health.)

Return the new current_health after health regeneration stops.
'''
import math

def regenerate(current_health, max_health, enemy_distance):
    while enemy_distance > 3:
        if current_health == max_health:
            return current_health
        current_health += 1
        enemy_distance -= 2
    return current_health

def regenerate(current_health, max_health, enemy_distance):
    if(enemy_distance <= 3):
        return current_health
    q = enemy_distance // 2 - 1
    return min(current_health + q, max_health)

run_cases = [(0, 10, 20, 9), (0, 10, 4, 1), (8, 10, 20, 10)]

submit_cases = run_cases + [
    (0, 0, 0, 0),
    (9, 10, 3, 9),
    (100, 100, 200, 100),
    (2, 110, 50, 26),
    (100, 1010, 2000, 1010),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print("Inputs:")
    print(f" * current_health: {input1}")
    print(f" *     max_health: {input2}")
    print(f" * enemy_distance: {input3}")
    print(f"Expected Health: {expected_output}")
    result = regenerate(input1, input2, input3)
    print(f"  Actual Health: {result}")
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

In the countdown_to_start function, write a loop that counts down from 10 to 1. At each iteration, print the number with an ellipsis:

i...

However, when i is 1, it should print 1...Fight! instead.
'''

def countdown_to_start():
    for i in range(10, 1, -1):
        print(f"{i}...")
    print("1...Fight!")


# Don't edit below this line


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()

'''
Assignment C2

In the calculate_flurry_crit function, write a loop that calculates and returns the total_damage of the flurry as a critical hit.

The function takes 2 inputs num_attacks, base_damage.

    Range over the num_attacks for the flurry
    Calculate the total damage for each attack within the flurry. Remember, each attack is a critical hit and does double the base_damage!
    The final swing of the flurry should do 4x the base_damage
    Return the total damage

'''

def calculate_flurry_crit(num_attacks, base_damage):
    if num_attacks == 0:
        return 0
    total_dmg = 0
    for i in range(0, num_attacks):
        total_dmg += 2*base_damage
    return total_dmg + 2*base_damage

run_cases = [
    (2, 5, 30),
    (3, 15, 120),
    (4, 30, 300),
    (0, 1, 0),
]

submit_cases = run_cases + [
    (1, 0, 0),
    (5, 50, 600),
    (7, 105, 1680),
    (10, 225, 4950),
    (15, 525, 16800),
    (20, 950, 39900),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Num attacks: {input1} Base damage: {input2}")
    print(f"Expecting: {expected_output} damage")
    result = calculate_flurry_crit(input1, input2)
    print(f"Actual: {result} damage")
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
Assignment C3

Complete the calculate_experience_points function.

The calculate_experience_points function takes a single parameter named level. Determine the total XP they have gained to reach the specified level from level 1 and return it.
'''

def calculate_experience_points(level):
    xp = 0
    for i in range(0, level):
        xp += 5 * i
    return xp

def calculate_experience_points(level):
    if(level == 1):
        return 0
    else:
        return 5 * (level-1) + calculate_experience_points(level - 1)
    
#xp(l) = 5*(l-1) + xp(l-1)
#xp(l-1) = 5*(l-2) + xp(l-2)
#can make a direct function

def calculate_experience_points(level):
    return 5 * level * (level - 1) // 2

run_cases = [
    (2, 5),
    (3, 15),
    (4, 30),
]

submit_cases = run_cases + [
    (1, 0),
    (5, 50),
    (7, 105),
    (10, 225),
    (15, 525),
    (20, 950),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = calculate_experience_points(input1)
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
Assignment C4

The team wants the random events to trigger on prime numbers. Write a function that takes a single number as input and returns True if it is a prime number or False if it is not.
'''

def is_prime(number):
    if(number < 2):
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

run_cases = [
    (7, True),
    (-7, False),
    (9, False),
    (23, True),
]

submit_cases = run_cases + [
    (-1, False),
    (0, False),
    (1, False),
    (2, True),
    (4, False),
    (31, True),
    (100, False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input number: {input1}")
    print(f"Expecting: {expected_output}")
    result = is_prime(input1)
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
Assignment C5

Complete the meditate function using a while loop. It takes mana, max_mana, energy and energy_drinks integers.

    While meditating, a character converts 1 energy into 1 mana for each iteration of the loop, up to the max_mana.
    If they have any energy_drinks when they run out of energy, they will drink 1 energy potion to gain 50 energy and continue meditating.
    A character will stop meditating when:
        Their mana reaches the max_mana, or
        They run out of both energy and energy_drinks.

Return the mana and remaining energy and energy_drinks when the character stops meditating.
'''

def meditate(mana, max_mana, energy, energy_drinks):
    while energy + mana < max_mana and energy_drinks > 0:
            energy += 50
            energy_drinks -= 1
    while mana < max_mana and energy > 0:
        mana += 1
        energy -= 1
    
    return mana, energy, energy_drinks

run_cases = [
    (0, 10, 9, 0, [9, 0, 0]),
    (0, 12, 0, 1, [12, 38, 0]),
    (1, 100, 99, 2, [100, 0, 2]),
]

submit_cases = run_cases + [
    (0, 0, 0, 0, [0, 0, 0]),
    (1000, 1000, 200, 5, [1000, 200, 5]),
    (0, 10, 0, 2, [10, 40, 1]),
    (5, 2000, 250, 6, [555, 0, 0]),
]


def test(input1, input2, input3, input4, expected):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" *           mana: {input1}")
    print(f" *       max_mana: {input2}")
    print(f" *         energy: {input3}")
    print(f" *  energy_drinks: {input4}")
    print(
        f"Expecting: mana {expected[0]}, energy {expected[1]}, energy drinks {expected[2]}"
    )
    result_mana, result_energy, result_drinks = meditate(input1, input2, input3, input4)
    print(
        f"   Actual: mana {result_mana}, energy {result_energy}, energy drinks {result_drinks}"
    )
    if (
        result_mana == expected[0]
        and result_energy == expected[1]
        and result_drinks == expected[2]
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
