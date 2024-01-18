# DNA Replication Game, Jahreem Jeffers, v0.0

# Import Entire Modules -- Get the whole tool box.
import time, datetime 

# Import Specific Methods -- Get the specific tool.
from random import choice

# Store the DNA bases
dnaBases = ["A", "T", "G", "C"]

# GAME FUNCTIONS
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please enter a positive integer number of bases to generate.\n"))
    dnaSequence = ""

    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    return dnaSequence

dna = genDNA()

def doTranscription(dnaSequence: str) -> tuple:

    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now generate RNA sequence that would match.\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence.\n")
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:000- UTC Jan. 01, 1970
    rnaSequence = input("Please enter the matching Rna sequence. Leave no spaces! Then press enter.\n").upper()
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime)
    # Tuples are ORDERED -- you can reference items with the index.
    # Tuples are UNCHANGABLE -- you cannot add, modify, or delete after creating
    # Tuples CAN have duplicate values.

def verifySequence(dnaSequence: str, rnaSequence:str) -> bool:
    isMatch = False
    if len(dnaSequence) != len(rnaSequence):
        print("The sequences are different lengths and cannot match.\n")
        return isMatch
    for dnaBase, rnaBase in zip(dnaSequence, rnaSequence):
        if dnaBase == "A" and rnaBase == "U":
            isMatch = True
        elif dnaBase == "C" and rnaBase == "G":
            isMatch = True
        elif dnaBase == "G" and rnaBase == "C":
            isMatch = True
        elif dnaBase == "T" and rnaBase == "A":
            isMatch = True
        else:
            print("error message about no match.\n")
    return isMatch

def calcScore(rnaSequence: str, rnaTime: float) -> int:
    score = 0
    if rnaTime < 1.0:
        score += 1000000
    elif rnaTime < 5.0:
        score += 900000
    elif rnaTime < 15.0:
        score += 700000
    elif rnaTime < 25.0:
        score += 500000
    else: # Slowest Time Lowest Score
        score +=25000
    return score

    scoreMulti = 0.0
    if len(rnaSequence) >= 30: 
        scoreMulti = 5.0
    if len(rnaSequence) >= 25: 
        scoreMulti = 4.0
    if len(rnaSequence) >= 20: 
        scoreMulti = 3.0
    if len(rnaSequence) >= 15: 
        scoreMulti = 2.0
    if len(rnaSequence) >= 5:
        scoreMulti = 1.0
    else:
        scoreMulti = 0.5
    # Increase score score, multiplier should be > 1.0
    #Decrease score,  multiplier should be < 1.0
    score *= scoreMulti
    return score

def saveScore(dnaSequence: str, rnaSequence: str, rnaTime: float, score: int) -> None:
    playerName = input("What is your first name?\n")
    lastName = input("What is your last name?\n")
    fullName = playerName + " " + lastName

    fileName = "dnaReplicationScore" + fullName + ".txt"
    saveData = open(fileName, "a")
    # File Modes
    # "X" mode -- CREATE FILE, IF FILE EXISTS, EXIT WITH ERROR
    # "W" mode -- CREATE FILE, IF FILE EXISTS, OVERWRITE IT
    # "A" mode -- CREATE FILE, IF FILE EXISTS, APPEND TO IT
    saveData.write(f"DNA Sequence: {dnaSequence}\n RNA Sequence {rnaSequence}\n")
    saveData.write(f"Transcripition Time: {rnaTime}\n")
    saveData.write(f"Score: {score}\n")
    saveData.write(f"{fullName}\n")
    saveData.write(f"{datetime.datetime.now()}\n")
    saveData.close()




dna = genDNA()
rna = doTranscription(dna)
if verifySequence(dna, rna[0]):
    score = (calcScore(rna[0] rna [1]))
    saveScore(dna, rna[0], rna[1], score)


