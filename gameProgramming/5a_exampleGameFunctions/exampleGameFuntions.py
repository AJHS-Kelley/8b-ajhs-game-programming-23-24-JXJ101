# Example Game Functions Project, Jahreem Jeffers, v0.0
import random

def functionaone():
    pass

def functionTwo(param1):
    pass

def functionThree(param1 = "Default Value"):
    pass

def functionFour(param1, param2, param3):
    pass
# Example to the funciton
# fighting game genre
# Function to get user input for characrter stats
def get_character_stats(character_name):
    '''
    Gets user input for character stats and returns a tuple of (health, attack, defense).
    Parameters:
    - character_name: The name of the character for which stats are being input.
    Returns:
    A tuple of (health, attack, defense).
    '''
    print(f"\nEnter the stats for (character_name):")
    health = int(input("Health: "))
    attack = int(input("Attack: "))
    defense = int(input("defense: "))
    return health, attack, defense

#  Function to compare two character stats
def compare_characters(char1_name, char1_stats, char2_name, char2_stats):
    """
    Compare the stats of 2 characters and prints the results.
    Parameters:
    - char1_name: Name of Character 1
    - char1_stats: Stats of Character 1 (tuple of health, attack, defense)
    - char2_name: Name of Character 2
    - char2_stats: Stats of Character 2 (tuple of health, attack, defense)
    """
    print(f"\nComparing Characters:")
    print(f"{char1_name}: {char1_stats}")
    print(f"char1_name}: {char2_stats}")
#def round(playerHealth, roundTime):
    #if playerHealth > 0 and roundTime > 0:
        #roundEnd = False
    #elif playerHealth <= 0 and roundTime <= 0
        #roundEnd = True
        
    #if roundEnd = True:
        #print("K.O") and RoundScore + 1         
    
#round(75, 0)
     
    
    
    
    
    
# Example to the funciton
# def catchBall(throwQuality, passCatchScore, weather):
 #   if throwQuality > 5.0 and passCatchScore >= and weather == 'Sunny':
 #       ballCaught = True
 #   elif throwQuality > 4.0 and passCatchScore >= 75 and weather == 'Windy':
 #       ballCaught =  false
 #   else:
 #       print('Oh, no, interception!\n')
 #       ballIntercepted = True
 #       return ballIntercepted
 #   return ballCaught

#catchBall(4.25, 107, 'Rainy')