# Select the secret number from a given range. 
# Player must guess the number.
# Compare guess to the secret number.
# What happens if the guess is wrong?
    # Tell them the guess is wrong. 
    # Tell them the number of guesses left.
    # Tell them if too high / too low.
# What happens if the guess is right?
    # Tell them guess is correct.
    # Award a point. 
# What happens if the player runs out of guesses?
    # Tell player round has been lost.
    # Award point to CPU.
# Check to see if player or CPU has >= 3 points, if so they win. 
import random # Import the random module to our code.

    

# DECLARATIONS 
secretNumber = -1
playerGuess = -1
playerScore = 0
cpuScore = 0
numGuesses = 0 # How many guesses they have taken. 
playerName = ""
difficulty = ""
rangeMin = 0
rangeMax = 0 
numAttempts = 4 # How many guesses they are allowed to have.  

print("""
        *~~~~~~~~~~~~~~~~~~~~~~~*
        |     Guess  a Number   |
        |         JXJ           |
        |                       |
        |        2023           |
        *~~~~~~~~~~~~~~~~~~~~~~~*

      """)
# CPU SECRET NUMBER GENERATION

secretNumber = random.randint(rangeMin,rangeMax)
    
    

# GAMELOOP
print("You need to guess a number from 0 to 20 and you have four guesses. \nIf you guess it right, you get a point. \nIf you get it wrong you lose a guess. \n lose all guesses the CPU get a point")
# ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH MATCH
# print() an explanation of your three difficulty levels.
# Use input () to store difficulty in difficulty variable
# assign values to numAttempts, rangeMin, and rangeMax based on choice.
#input(1)
difficulty = input("type what difficulty you want to choose")
print(f"you chose {difficulty} is that correct?")
isCorrect = input("Please type yes if correct, no if not correct.\n")
if isCorrect == "yes":
        print(f"Ok {playerName}, let's continue!")

print(f"Player Score: {playerScore}\nCPU: {cpuScore}.\n")
    secretNumber = random.randint(rangeMin, rangeMax)
    # print(secret_number)
    # You do not ask the player to input a difficulty.  
if difficulty == "easy": 
        rangeMin = 0 
        rangeMax = 10
        numAttempts = 4
elif difficulty == "medium":
        rangeMin = 0
        rangeMax = 30
        numAttempts = 4
elif difficulty == "hard":
        rangeMin = 0
        rangeMax = 50
        numAttempts = 2
else: 
        pass
while playerScore != 3  and cpuScore != 3:

        # playerName = input("choose the difficulty\n Type the difficulty you want to choose and press Enter.\n")
        # Print that the difficulty could not be matched, provide default values.
        


    
    
    for guesses in range(numAttempts): # What can you replace the 4 with to make the number of guesses change to reflect the difficulty?  
        print(f"You have {numAttempts - numGuesses} guesses remaining\n")
        playerGuess = int(input("Type a number from 0 to 20 and press ENTER.\n"))
        # input() saves all data as a STRING by default
        # int() will convert to a integer
        # float() will convert to a FLOAT
        print(f"You have chosen {playerGuess}. Let's see if you're right!\n")
        if playerGuess == secretNumber:
            playerScore  += 1 
            print("Whoa dude, what a guess! You got it!\n")
            break # IMMEDIATELY EXIT ANY LOOP YOU ARE IN!
        else:
            print("You did not guess correctly. Idiot.\n")
            if playerGuess > secretNumber:
                print("Your guess is too high.\n")
            else:
                print("Your guess is too low.\n")
        numGuesses += 1
    if playerGuess != secretNumber:
        cpuScore += 1 
        print("The CPU wins a point since you ran out of guesses.\n")
        
if playerScore >3:
    print("Winner, winner, chicken dinner! You scored 3 points first!\n")
else:
    print("Yo, you lost to a computer. You are a scrub.\n")