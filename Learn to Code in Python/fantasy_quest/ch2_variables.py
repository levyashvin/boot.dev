num_bananas = 10
f_string = f"You have {num_bananas} bananas"
print(f_string)
# You have 10 bananas

name = "Yarl"
age = 37
race = "dwarf"

# Don't edit above this line

print(f"{name} is a {race} who is {age} years old.")

# create the empty "enemy" variable here
enemy = None

# don't touch below this line
print(enemy is None)

print(type(enemy))

sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line

print(sentence_start + player1_health + sentence_end)
print(sentence_start + player2_health + sentence_end)

sword_name, sword_damage, sword_length = "Excalibur", 10, 200
a, b = 1, 2
a, b = b, a

'''
Expected O/P:
You there! Adventurer!
The local mine has been taken over by orcs!
We need your help taking it back. Bring back 8 of their axes as proof of your hard work.
'''
quest_start = "You there! Adventurer!"
quest_middle = "The local mine has been taken over by orcs!"
quest_end = "We need your help taking it back."
quest_objective = "Bring back 8 of their axes as proof of your hard work."
space = " "

# don't touch above this line
print(quest_start)
print(quest_middle)
print(quest_end + space + quest_objective)

'''
Assignment

Competitive Fantasy Quest players - Ballan's Ballers - have won all their games in the elimination round of the tournament. They're now in the finals! Calculate the average score of their 4 games and store it in the average_score variable.

The average (or "mean") is calculated by adding up all the numbers and dividing by how many numbers there are. Which means first we need to add up all the scores, then divide by 4.

Let's use our spellbook to recall the syntax we need:

    Look at the bottom-right of the lesson text, you'll see a toggle to switch from Boots to your spellbook. Flip the switch to open your spellbook.
    Search for the concept you'll need for this lesson, maybe "python math" or "order of operations"
    Complete the lesson using your spellbook as a reference

'''

game_one_score = 97
game_two_score = 92
game_three_score = 106
game_four_score = 105

# Don't touch above this line

average_score = (game_one_score + game_two_score + game_three_score + game_four_score) / 4

# Don't touch below this line

print(round(average_score))

'''
Assignment

Fix the bugs and get the character report working!

    Update the variables to their expected data types:

    name: string
    level: integer
    character_class: string
    armor: integer
    magic_resistance: float
    account_active: boolean

    Fix the bug with the f-string on line 9.

'''

name = "Lopen"
level = 25
character_class = "Windrunner"
armor = 12
magic_resistance = 15.4
account_active = True

print("Character Report")
print(f"{name} is a level {level} {character_class}.")
print(f"They have {armor} armor and {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

# Don't edit below this line

print("=========================")
print("Character Report Complete")
print("Data types:")
print(
    f"name: {type(name).__name__}, level: {type(level).__name__}, character_class: {type(character_class).__name__}"
)
print(
    f"armor: {type(armor).__name__}, magic_resistance: {type(magic_resistance).__name__}"
)
print(f"account_active: {type(account_active).__name__}")
