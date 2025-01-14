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
