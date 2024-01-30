# Dice rolling module by Jahreem Jeffers, V0.0
import random

def roll(numDice, sizeDice): # Verified working 12/14/23
    numRolled = 0
	sum = 0
    while numRolled < numDice
	    roll = random.randint(1, sizeDice)
		sum += roll
		numRolled += 1
	return sum

def display(numDice, sizeDice):
    numRolled = 0
	sum = 0
    while numRolled < numDice
	    roll = random.randint(1, sizeDice)
		sum += roll
		print(f"Roll:{roll}\n")
		print(f"sum:{sum}\n")
		numRolled += 1
	return sum

def isDoubles(roll1, roll2):
    if roll1 == roll2:
        isDoubles =  True
        else:
            isDoubles = false
        return isDoubles



