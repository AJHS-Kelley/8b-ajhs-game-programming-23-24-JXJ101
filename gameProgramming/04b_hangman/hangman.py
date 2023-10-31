# Hangman Game by jahreem Jeffers v0.1
import random

words = 'tricky hank pico whitty tabi agoti matt sans paparus gaster steve alex pepinno aiden jaiden chrisly blaze melina jason max rex chara doomslayer kratos thor madmax void carol hex johnnycage'.split()

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
     ========''']
     
# Pick Word from List
def getRandomWord(wordList): # Return a random word from the list.
    wordIndex = random.randint(0,len(wordList)- 1)
    #len(listName - 1 is EXTREMELY COMMON FOR WORKING FOR LISTS.
    return wordList[wordIndex]
    
i = 0
while i < 100:
    word = getRandomWord(words)
    print(word)
    i += 1