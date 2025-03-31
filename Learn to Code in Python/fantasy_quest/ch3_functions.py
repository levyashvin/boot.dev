'''
Assignment L1

We need to calculate the size of a weapon's "attack area". With a 1.0 meter sword, for example, a player can attack in an area of 3.14 square meters around them. You can use the area_of_circle function to do that calculation.

Fix the bug on line 13 by calling the area_of_circle function with the spear_length as input and store the result in the spear_area variable.
'''

def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
spear_length = 2.0

# don't touch above this line

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

# don't touch below this line

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")

'''
Assignment L5

We need to calculate the total damage from a combo of three damaging attacks. Complete the triple_attack function by returning the sum of its parameters, damage_one, damage_two, and damage_three.

The attacks (attack_one to attack_six) are already passed to two triple_attack functions for you, so you do not need to use them directly in the function.
'''

def triple_attack(damage_one, damage_two, damage_three):
    return damage_one + damage_two + damage_three

# Don't touch below this line

# This is the first triple attack
attack_one = 2
attack_two = 4
attack_three = 3
first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

print("Getting damage for", attack_one, attack_two, "and", attack_three, "...")
print(first_triple_attack_damage, "points of damage dealt!")
print("=====================================")

# This is the second triple attack
attack_four = -1
attack_five = 10
attack_six = 5
second_triple_attack_damage = triple_attack(attack_four, attack_five, attack_six)

print("Getting damage for", attack_four, attack_five, "and", attack_six, "...")
print(second_triple_attack_damage, "points of damage dealt!")
print("=====================================")

'''
Assignment L6

There's a problem in the get_title function! It's supposed to calculate the title value and return it to the caller. Instead, it's barbarically printing the value to the console.

Fix the function so that it returns the title instead of printing it to the console.
'''

def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return title


# Don't touch below this line


def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")

'''
Assignment L7

There's a bug! Run the code and read the printed error, then fix it.
'''

def main():
    print("Fantasy Quest is booting up...")
    print("Game is running!")

main()

'''
Assignment L11

Enough Discord talk, back to writing code.

In Fantasy Quest, characters lose health due to heat exhaustion. The game tracks the temperature in Freedom units (Fahrenheit), but we need to display the temperature in Celsius for players outside the US. Here's the formula to calculate the temperature in Celsius from Fahrenheit (f):

5/9 * (f - 32)

Complete the to_celsius function body. It should return the temperature in Celsius for a given Fahrenheit temperature (f parameter).
'''

def to_celsius(f):
    return 5/9 * (f - 32)


## Don't touch below this line


def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")


test(100)
test(88)
test(104)
test(112)

'''
Assignment L15

Enough about solution mechanics, let's write more code.

We need to display the current time to our players. The problem is that the time is stored as a number of hours, but we want to display it as a number of seconds. There are 60 seconds in a minute, but how many are in an hour?

Complete the hours_to_seconds function. It should convert hours to seconds and return the result.
'''

def hours_to_seconds(hours):
    return hours * 3600


# Don't touch below this line


def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(25)
test(100)
test(33)

'''
Assignment L18

Complete the become_warrior function. It accepts 2 inputs: the full_name string, and the power integer. It should return 2 values: a "title" string and a "new power" integer.
'''

def become_warrior(full_name, power):
    title = full_name + " the  warrior"
    new_power = power + 1
    return title, new_power


# Don't edit below this line


def main():
    test("Frodo Baggins", 5)
    test("Bilbo Baggins", 10)
    test("Gandalf The Grey", 9000)


def test(input1, input2):
    result1, result2 = become_warrior(input1, input2)
    print(result1, "has a power level of:", result2)


main()

'''
Assignment L21

Complete the get_punched and get_slashed functions. They should both:

    Take 2 integers as arguments, health and armor
    Set armor to a default value of 0

get_punched

    Create a damage variable equal to 50 minus the armor - the armor reduces the damage
    Create a new_health variable equal to the input health minus damage - we apply the damage
    Return new_health

get_slashed

    Create a damage variable equal to 100 minus the armor
    Create a new_health variable equal to the input health minus damage
    Return new_health

'''

def get_punched(health, armor = 0):
    dmg = 50 - armor
    new_health = health - dmg
    return new_health


def get_slashed(health, armor = 0):
    dmg = 100 - armor
    new_health = health - dmg
    return new_health


# Don't touch below this line


def test(health, armor):
    print(f"Running tests for health {health} and armor {armor}")
    print("========================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("----------------------------------------\n")


test(400, 5)
test(300, 3)
test(200, 1)

'''
Assignment C1

Complete the curse function. It accepts a weapon_damage parameter and returns two values:

    The lesser_cursed damage: reduce the input weapon_damage from 100% to 50% (50% reduction).
    The greater_cursed damage: reduce the input weapon_damage from 100% to 25% (75% reduction).

A greater curse is more powerful than a lesser curse, so it reduces the damage more.
'''

def curse(weapon_damage):
    lesser_cursed = weapon_damage / 2
    greater_cursed = weapon_damage / 4
    return lesser_cursed, greater_cursed

# Don't modify below this line


def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("=====================================")


def main():
    test(100)
    test(500)
    test(1000)


main()

'''
Assignment C2

Complete the enchant_and_attack function. It creates a new "enchanted" name for a weapon and calculates how much damage the enchanted weapon will deal to a targeted enemy.

It accepts 3 parameters:

    target_health: integer
    damage: integer
    weapon: string

It should do the following things in the function body:

    Calculate and store the "enchanted damage" in a new variable. The enchanted damage should be the input damage plus 10.
    Calculate and store the "new health" in a new variable. The new health should be the input target_health minus the enchanted damage.
    Create a new variable called enchanted_weapon. It should be the input weapon with the string "enchanted " added to the beginning of it. For example:
        sword -> enchanted sword
        axe -> enchanted axe
    Return the enchanted weapon and the new health in that order.

'''

def enchant_and_attack(target_health, damage, weapon):
    enchanted_dmg = damage + 10
    new_health = target_health - enchanted_dmg
    enchanted_weapon = "enchanted " + weapon
    return enchanted_weapon, new_health


# Don't modify below this line


def test(target_health, damage, weapon):
    print(f"The target has {target_health} health.")
    print(f"{weapon} base damage: {damage} - Enchanting and attacking.")
    enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
    print(f"The target has been attacked with the {enchanted_weapon}.")
    print(f"The target has {new_health} health remaining.")
    print("=====================================")


def main():
    test(100, 50, "sword")
    test(500, 100, "axe")
    test(1000, 250, "bow")


main()
