#Assignment We need to keep track of our hero's health! On the first line of code, create a new variable named player_health and set it equal to 1000.

#player_health = 1000 
# don't touch below this line

print(player_health)


#Assignment
#We need to reduce our hero's health as they take damage.
#Before each print() function in the provided code, change the value of player_health to 100 less than it was before.
#The final output should look like this:
```bash
900
800
700
600
```
#player_health = 1000

# reduce by 100 here

#player_health = 100
#print(player_health)

# and here
player_health = 900
print(player_health)

# and here
player_health = 800
print(player_health)

# and here
player_health = 700
print(player_health)

# and here
player_health = 600
print(player_health)

#Assignment
#Create a new variable called armored_health on line 4 and set it equal to player_health * armor_multiplier

player_health = 1000
armor_multiplier = 2

armored_health = player_health * armor_multiplier
# create armored_health here
print(armored_health)

#Assignment
#When our hero walks through poison, their health should go down. Right now the hero is gaining 10 health instead of losing 10 health. Change the poison_damage variable to be negative.

player_health = 100
poison_damage = -10

# don't touch below this line

player_poison_health = player_health + poison_damage

print(player_poison_health)

#Assignment
#Line #1 in the code was meant to be a comment, but the developer forgot to use the correct syntax (#).
#Fix the bug by commenting out the first line of code.

#the best_sword variable holds the value of the best sword in the game
best_sword = "scimitar"
print(best_sword)

#Assignment
#Fix the bugs in the code. player_health should be an integer and player_has_magic should be a boolean.
player_health = 100

player_has_magic = True

# don't touch below this line
print(f"player_health is a/an {type(player_health).__name__}")
print(f"player_has_magic is a/an {type(player_has_magic).__name__}")

#Assignment

#Fix the bug on line 7. Use an f-string to inject the dynamic values into the string:
#Replace NAME with the value of the name variable
#Replace RACE with the value of the race variable
#Replace AGE with the value of the age variable
#Do not "hard-code" the values into the string. For example, this is not the solution we're looking for (even though it happens to work in this case):
#print("Yarl is a dwarf who is 37 years old.")
#We need the player to see their values.
name = "Yarl"
age = 37
race = "dwarf"

# Don't edit above this line

print(f"{name} is a {race} who is {age} years old.")

#Assignment
#Declare a variable named enemy and set it to None. Don't change the print() function.
# create the empty "enemy" variable here
enemy = None
# don't touch below this line
print(enemy is None)

# Assignment
# We have a second player in our game!
# We need to tell each of our players how much health they have left.
# Edit line 9 to print Player 1’s health: You have 1200 health using string concatenation and the variables provided
# Edit line 10 to print Player 2’s health: You have 1100 health in the same way
# Only print “You have x health” once for each player, nothing else.

sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line

print(sentence_start + player1_health + sentence_end)
print(sentence_start + player2_health + sentence_end)
