# Hangman Game by jahreem Jeffers v0.1
import random

#words = 'tricky hank pico whitty tabi agoti matt sans paparus gaster steve alex pepinno aiden jaiden chrisly blaze melina jason max rex chara doomslayer kratos thor madmax void carol hex johnnycage'.split()
# DICTIONARY VERSION
# Stored in Key:Value Pairs.
# Actual Dictionary Woes (Key) : Value (Definition)
# Uses {} to specify a dictionary
words = {'Colors': 'Red orange yellow Green yellow blue indigo violet fuchia teal garnet gold black white silver gray'.split(),
        'Animals': 'cat cow dog moose goose fish wombat wolverine giraffe wolf lion alligator'.split(),
        'Shapes': 'square triangle circle rhombus parallogram trapeziod diamond dodecahedron'.split(),
        'Foods': 'hamburger hotdog potato waffle pancake escargot oysters chips steak'.split()}


# VARIABLE_NAME in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
        |
        |
        |
     ========''', '''
     +---+
     0  |
        |
        |
     ========''', '''
     +---+
     0  |
     |  |
        |
     ========''', '''
     +---+
     0  |
    /|  |
        |
     ========''', '''
    
     +---+
     0  |
    /|\ |
        |
     ========''', '''
     +---+
     0  |
    /|\ |
    /   |
     ========''', '''
     +---+
     0  |
    /|\ |
    / \ |
     ========''', '''
     +---+
     0  |
   o-|-o|
    / \ |
     ========''', '''
     +---+
     0   |
   o-|-o |
    / \  |
   o   o |
     ========''']
     
# Pick Word from List
#def getRandomWord(wordList): # Return a random word from the list.
    #wordIndex = random.randint(0,len(wordList)- 1)
    #len(listName - 1 is EXTREMELY COMMON FOR WORKING FOR LISTS.
    #return wordList[wordIndex]
 # Pick Word from Dictionary
 
def getRandomWord(wordDict): # Return a random word from the list.
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0,len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]
    
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()
    
    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()
    
    blanks = '_' * len(secretWord)
    
    # Replace Blanks with Correct Letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:] 
            
    for letter in blanks:
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Please guess a letter and press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('Letter has been guessed already, try again.')
        elif guess not in 'abcdefghijklmnopqurstuvwxyz':
            print('Please guess a LETTER from the English alphabet.')
        else:
            return guess

def playAgain():
    print('Do you want to play Again? Yes or No?')
    return input().lower().startswith('y')

# Introduce the Game
print('Welcome to Hangman by your host JXJ!')
# CHOOSE DIFFICULTY
difficulty = 'X'
while difficulty not in 'EMH':
    print('Please Choose Easy, Medium or Hard. Type the first letter then press enter.\n')
    difficulty = input().upper()
if difficulty == 'M': #medium
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
if difficulty == 'H': # Hard
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
    del HANGMAN_BOARD[5]
    del HANGMAN_BOARD[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

# Main Game Loop
while True:
    print('The secret word is from the ' + secretSet + ' category.\n')
    displayBoard(missedLetters, correctLetters, secretWord)
    
    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters = correctLetters + guess
        
        # Check To See If Winner, Winner Chicken Dinner
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters: # if True: 
            print('congrats, you have won this time.')
            print('The secret word was' + secretWord)
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        
        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses and lost the game. Shame')
            print('You made this number of correct guesses' + str(len(correctLetters)))
            print('The secret word was' + secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain(): 
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretset = getRandomWord(words)
        else:
            break


#i = 0
#while i < 100:
    #word = getRandomWord(words)
    #print(word)
    #i += 1
    
    
