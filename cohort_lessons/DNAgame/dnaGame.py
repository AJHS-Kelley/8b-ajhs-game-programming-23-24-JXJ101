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

def genRNA(dnaSequence: str) -> tuple:
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now generate RNA sequence that would match.\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence.\n")
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:000- UTC Jan. 01, 1970
    rnaSequence = input("Please enter the matching Rna sequence. Leave no spaces! Then press enter.\n")
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime)
    # Tuples are ORDERED -- you can reference items with the index.
    # Tuples are UNCHANGABLE -- you cannot add, modify, or delete after creating
    # Tuples CAN have duplicate values.

rna = genRNA(dna)
print(rna)

