'''
Assignment L1

Complete the get_character_record function. It takes a character's name, server, level, and rank as individual inputs, and returns a dictionary with the following string keys:

    "name"
    "server"
    "level"
    "rank"
    "id"

Create and return a dictionary with the keys above. Assign each of the four inputs to the matching key, ie: "name": name.

Next, we can't have two characters named bloodwarrior123's on the same server! For the fifth key, id, create a unique value as follows:

Concatenate the name and the server inputs with a # in the middle. For example, given:

    name = "bloodwarrior123"
    server = "server1"

Then the id field would be set to bloodwarrior123#server1.
'''

def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": name + "#" + server
    }

run_cases = [
    (
        "bloodwarrior123",
        "server1",
        5,
        1,
        {
            "name": "bloodwarrior123",
            "server": "server1",
            "level": 5,
            "rank": 1,
            "id": "bloodwarrior123#server1",
        },
    ),
    (
        "fronzenboi",
        "server2",
        2,
        1,
        {
            "name": "fronzenboi",
            "server": "server2",
            "level": 2,
            "rank": 1,
            "id": "fronzenboi#server2",
        },
    ),
]

submit_cases = run_cases + [
    (
        "slasher69",
        "server3",
        2,
        5,
        {
            "name": "slasher69",
            "server": "server3",
            "level": 2,
            "rank": 5,
            "id": "slasher69#server3",
        },
    ),
    (
        "icequeen",
        "server4",
        3,
        2,
        {
            "name": "icequeen",
            "server": "server4",
            "level": 3,
            "rank": 2,
            "id": "icequeen#server4",
        },
    ),
    (
        "shadowmaster",
        "server5",
        4,
        3,
        {
            "name": "shadowmaster",
            "server": "server5",
            "level": 4,
            "rank": 3,
            "id": "shadowmaster#server5",
        },
    ),
    (
        "silentslasher",
        "server6",
        5,
        4,
        {
            "name": "silentslasher",
            "server": "server6",
            "level": 5,
            "rank": 4,
            "id": "silentslasher#server6",
        },
    ),
    (
        "hypershadow",
        "server7",
        3,
        5,
        {
            "name": "hypershadow",
            "server": "server7",
            "level": 3,
            "rank": 5,
            "id": "hypershadow#server7",
        },
    ),
]


def test(name, server, level, rank, expected_output):
    try:
        result = get_character_record(name, server, level, rank)
        for key, value in expected_output.items():
            print(f"Expected: {key}: {value}")
            print(f"Actual:   {key}: {result[key]}\n")
            if result[key] != value:
                if type(result[key]) != type(value):
                    print(f"'{key}' values are different types!")
                    print(
                        f"Expected '{key}' to be of type {type(value).__name__}, but got {type(result[key]).__name__}"
                    )
                print("Fail")
                return False
        if result != expected_output:
            print("Result object is incorrect:")
            for key, value in result.items():
                print(f" * {key}: {value}")
            print("Fail")
            return False
        print("Pass")
        return True
    except Exception as e:
        print(f"Exception: {str(e)}")
        print("Fail")
        return False


def main():
    index = 0
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        index += 1
        print("---------------------------------")
        print(f"Test Case #{index}\n")
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

Another developer on our team has introduced a bug by specifying duplicate keys in the dictionary! Fix the bug.

The get_character_record function takes a character's name, server, level, and rank. It should return a dictionary with the following fields:

    name
    server
    level
    rank
    id

Where the id is the name and the server concatenated together with a # in the middle for uniqueness. We can't have two bloodwarrior123's on the same server!
'''

def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }

run_cases = [
    (
        "bloodwarrior123",
        "server1",
        5,
        1,
        {
            "name": "bloodwarrior123",
            "server": "server1",
            "level": 5,
            "rank": 1,
            "id": "bloodwarrior123#server1",
        },
    ),
    (
        "fronzenboi",
        "server2",
        2,
        1,
        {
            "name": "fronzenboi",
            "server": "server2",
            "level": 2,
            "rank": 1,
            "id": "fronzenboi#server2",
        },
    ),
]

submit_cases = run_cases + [
    (
        "slasher69",
        "server3",
        2,
        5,
        {
            "name": "slasher69",
            "server": "server3",
            "level": 2,
            "rank": 5,
            "id": "slasher69#server3",
        },
    ),
    (
        "kingofgames",
        "server4",
        3,
        2,
        {
            "name": "kingofgames",
            "server": "server4",
            "level": 3,
            "rank": 2,
            "id": "kingofgames#server4",
        },
    ),
    (
        "godofwar",
        "server5",
        1,
        5,
        {
            "name": "godofwar",
            "server": "server5",
            "level": 1,
            "rank": 5,
            "id": "godofwar#server5",
        },
    ),
    (
        "pythonista",
        "server6",
        4,
        3,
        {
            "name": "pythonista",
            "server": "server6",
            "level": 4,
            "rank": 3,
            "id": "pythonista#server6",
        },
    ),
    (
        "codemaster",
        "server7",
        3,
        1,
        {
            "name": "codemaster",
            "server": "server7",
            "level": 3,
            "rank": 1,
            "id": "codemaster#server7",
        },
    ),
]


def test(input1, input2, input3, input4, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
    print(f"Expecting: {expected_output}")
    result = get_character_record(input1, input2, input3, input4)
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

We need to be able to report to our players how many enemies are in their immediate vicinity - but they want the count of each enemy by its kind.

If you run the code, it will result in a KeyError.

Fix the count_enemies function. It takes a list of enemy_names as input. It should return a dictionary where the keys are all the enemy names from the list, and the values are the counts of how many times each enemy appeared in the list.
'''

def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in set(enemy_names):
        enemies_dict[enemy_name] = 0
    for enemy_name in enemy_names:
        enemies_dict[enemy_name] += 1
    return enemies_dict

run_cases = [
    (["jackal", "kobold", "soldier"], {"jackal": 1, "kobold": 1, "soldier": 1}),
    (["jackal", "kobold", "jackal"], {"jackal": 2, "kobold": 1}),
]

submit_cases = run_cases + [
    ([], {}),
    (["jackal"], {"jackal": 1}),
    (
        [
            "jackal",
            "kobold",
            "jackal",
            "kobold",
            "soldier",
            "kobold",
            "soldier",
            "soldier",
            "jackal",
            "jackal",
            "gremlin",
            "jackal",
            "jackal",
        ],
        {"jackal": 6, "kobold": 3, "soldier": 3, "gremlin": 1},
    ),
    (["jackal", "kobold", "gremlin"], {"jackal": 1, "kobold": 1, "gremlin": 1}),
    (["jackal", "jackal", "jackal"], {"jackal": 3}),
    (["gremlin", "gremlin", "gremlin"], {"gremlin": 3}),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = count_enemies(input1)
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

We need to display on our player's screens what the most common enemy in a given area of the game map is.

Complete the get_most_common_enemy function by iterating over all enemies in the dictionary and returning only the name of the enemy with the highest count.

If there are no enemies, return a None value. If there are multiple enemies with the same highest count, return the first one found.

enemies_dict is a dictionary of name -> count. Example:

{
    "jackal": 1,
    "kobold": 2,
    "soldier": 3,
    "gremlin": 5
}

Tip: Negative Infinity

When you're trying to find a "max" value, it helps to keep track of the "max so far" in a variable and to start that variable at the lowest possible number, negative infinity.

max_so_far = float("-inf")

You'll also want to keep track of the enemy name associated with the maximum count. I would set the default for that variable to None.
'''

def get_most_common_enemy(enemies_dict):
    common_enemy = None
    enemies_dict[None] = -1
    for enemy in enemies_dict:
        if enemies_dict[enemy] > enemies_dict[common_enemy]:
            common_enemy = enemy
    return common_enemy
            
run_cases = [
    ({"jackal": 4, "kobold": 3, "soldier": 10, "gremlin": 5}, "soldier"),
    ({"jackal": 1, "kobold": 3, "soldier": 2, "gremlin": 5}, "gremlin"),
]

submit_cases = run_cases + [
    ({"jackal": 2, "gremlin": 7}, "gremlin"),
    ({"jackal": 3}, "jackal"),
    ({}, None),
    ({"kobold": 5, "soldier": 5, "gremlin": 5, "dragon": 5}, "kobold"),
    ({"jackal": 5, "kobold": 3, "soldier": 10, "gremlin": 5, "dragon": 20}, "dragon"),
    ({"jackal": 5, "kobold": 3, "soldier": 2, "gremlin": 10, "dragon": 1}, "gremlin"),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_most_common_enemy(input1)
    if result == "None":
        print('Actual: "None"')
    else:
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

Complete the get_quest_status function. It accepts a progress dictionary (structure defined above) and returns the character's status in the "bridge_run" quest.
'''

def get_quest_status(progress):
    return progress["entity"]["character"]["quests"]["bridge_run"]["status"]

run_cases = [
    (
        {
            "entity": {
                "character": {
                    "name": "Sir Galahad",
                    "quests": {
                        "bridge_run": {
                            "status": "In Progress",
                        },
                        "talk_to_syl": {
                            "status": "Completed",
                        },
                    },
                }
            }
        },
        "In Progress",
    ),
    (
        {
            "entity": {
                "character": {
                    "name": "Lady Gwen",
                    "quests": {
                        "bridge_run": {
                            "status": "Completed",
                        },
                        "talk_to_syl": {
                            "status": "In Progress",
                        },
                    },
                }
            }
        },
        "Completed",
    ),
]

submit_cases = run_cases + [
    (
        {
            "entity": {
                "character": {
                    "name": "Archer Finn",
                    "quests": {
                        "bridge_run": {
                            "status": "Not Started",
                        },
                        "talk_to_syl": {
                            "status": "Completed",
                        },
                    },
                }
            }
        },
        "Not Started",
    ),
    (
        {
            "entity": {
                "character": {
                    "name": "Mage Elara",
                    "quests": {
                        "bridge_run": {
                            "status": "Failed",
                        },
                        "talk_to_syl": {
                            "status": "Completed",
                        },
                    },
                }
            }
        },
        "Failed",
    ),
    (
        {
            "entity": {
                "character": {
                    "name": "Rogue Talon",
                    "quests": {
                        "bridge_run": {
                            "status": "Completed",
                        },
                        "talk_to_syl": {
                            "status": "Not Started",
                        },
                    },
                }
            }
        },
        "Completed",
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Progress Dictionary: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_quest_status(input1)
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

Complete the merge function. It accepts two dictionaries as input and returns a single merged dictionary that contains all the keys and values from the input dictionaries.

If a key exists in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary. Here's the example usage:

two_towers = {"Frodo": 56, "Aragorn": 10}
rotk = {"Aragorn": 100, "Gandalf": 809}
merged_dict = merge(two_towers, rotk)
print(merged_dict)
# Output: {'Frodo': 56, 'Aragorn': 100, 'Gandalf': 809}

Notice how the key Aragorn's value gets overridden. His sword got upgraded.
'''

def merge(dict1, dict2):
    dict12 = {key:dict1[key] for key in dict1}
    for key in dict2:
        dict12[key] = dict2[key]
    return dict12

run_cases = [
    (
        {"Goku": 8000, "Vegeta": 7500},
        {"Piccolo": 3500, "Gohan": 2800},
        {
            "Goku": 8000,
            "Vegeta": 7500,
            "Piccolo": 3500,
            "Gohan": 2800,
        },
    ),
    (
        {"Frieza": 120000, "Cell": 900000},
        {"Majin_Buu": 1100000, "Broly": 10000},
        {
            "Frieza": 120000,
            "Cell": 900000,
            "Majin_Buu": 1100000,
            "Broly": 10000,
        },
    ),
]

submit_cases = run_cases + [
    ({}, {}, {}),
    (
        {
            "Android_17": 30000,
            "Android_18": 30000,
            "Future_Trunks": 9000,
            "Kid_Trunks": 7000,
        },
        {
            "Android_16": 40000,
            "Dr_Gero": 10000,
            "Goten": 6500,
            "Future_Gohan": 8000,
        },
        {
            "Android_17": 30000,
            "Android_18": 30000,
            "Android_16": 40000,
            "Dr_Gero": 10000,
            "Future_Trunks": 9000,
            "Kid_Trunks": 7000,
            "Goten": 6500,
            "Future_Gohan": 8000,
        },
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * first_half: {input1}")
    print(f" * second_half: {input2}")
    result = merge(input1, input2)
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