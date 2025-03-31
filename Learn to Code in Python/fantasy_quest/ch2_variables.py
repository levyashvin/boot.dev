'''
Assignment L1

We need to keep track of our hero's health!

On the first line of code, create a new variable named player_health and set it equal to 1000.
'''

player_health = 1000


# don't touch below this line

print(player_health)

'''
Assignment L2

We need to reduce our hero's health as they take damage.

Before each print() function in the provided code, change the value of player_health to 100 less than it was before.
'''

player_health = 1000
player_health -= 100
# reduce by 100 here

print(player_health)
player_health -= 100
# and here

print(player_health)
player_health -= 100
# and here

print(player_health)
player_health -= 100
# and here

print(player_health)

'''
Assignment L3

Create a new variable called armored_health on line 4 and set it equal to player_health * armor_multiplier
'''

player_health = 1000
armor_multiplier = 2
armored_health = player_health * 2

# create armored_health here
print(armored_health)

'''
Assignment L4

When our hero walks through poison, their health should go down. Right now the hero is gaining 10 health instead of losing 10 health. Change the poison_damage variable to be negative.
'''

player_health = 100
poison_damage = 10

# don't touch below this line

player_poison_health = player_health - poison_damage

print(player_poison_health)

'''
Assignment L5

Line #1 in the code was meant to be a comment, but the developer forgot to use the correct syntax (#).
'''

#the best_sword variable holds the value of the best sword in the game
best_sword = "scimitar"
print(best_sword)

'''
Assignment L8

Fix the bugs in the code. player_health should be an integer and player_has_magic should be a boolean.
'''

player_health = 100

player_has_magic = True

# don't touch below this line
print("player_health is a/an ", type(player_health).__name__)
print("player_has_magic is a/an ", type(player_has_magic).__name__)

'''
Assignment L9

Fix the bug on line 7. Use an f-string to inject the dynamic values into the string:

    Replace NAME with the value of the name variable
    Replace RACE with the value of the race variable
    Replace AGE with the value of the age variable

'''

name = "Yarl"
age = 37
race = "dwarf"

# Don't edit above this line

print(f"{name} is a {race} who is {age} years old.")

'''
Assignment L10

Declare a variable named enemy and set it to None. Don't change the print() function.
'''

# create the empty "enemy" variable here
enemy = None

# don't touch below this line
print(enemy is None)

'''
Assignment L14

We have a second player in our game!

We need to tell each of our players how much health they have left.

    Edit line 9 to print Player 1's health: You have 1200 health using string concatenation and the variables provided
    Edit line 10 to print Player 2's health: You have 1100 health in the same way

'''

sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line

print(sentence_start + player1_health + sentence_end)
print(sentence_start + player2_health + sentence_end)

'''
Assignment L17

Fantasy Quest's dialogue messages are all jumbled up. Fix it!

    Run the code. Notice that nothing prints to the console.
    Ask Boots why nothing is printing. You'll need to pay up (just do it). Be sure to click the clipboard icon on the text input to include your code so that he can see it.
    Use Boots to figure out what's wrong, fix the code, then submit it. We're expecting the following output:

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
Assignment L18

Competitive Fantasy Quest players – Ballan's Ballers – have won all their games in the elimination round of the tournament. They're now in the finals! Calculate the average score of their 4 games and store it in the average_score variable.

The average (or "mean") is calculated by adding up all the numbers and dividing by how many numbers there are. Which means first we need to add up all the scores, then divide by 4.
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
Assignment C1

Fix the bugs and get the character report working!

    Update the variables to their expected data types:

    name: string
    level: integer
    character_class: string
    armor: integer
    magic_resistance: float
    account_active: boolean

    Fix the bug with the f-string on line 9.

Original Values

name = "Lopen"
level = "25"
character_class = Windrunner
armor = 12.0
magic_resistance = 15.4
account_active = "True"

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
