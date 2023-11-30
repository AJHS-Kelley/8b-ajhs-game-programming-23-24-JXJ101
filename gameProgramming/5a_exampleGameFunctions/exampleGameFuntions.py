# Example Game Functions Project, Jahreem Jeffers, v0.9 W.I.P code wont start but its not broken :(
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
# Function to get user input for character stats 

def get_character_stats(character_name): 

    """ 

    Gets user input for character stats and returns a tuple of (health, attack, defense). 

    Parameters: 

    - character_name: The name of the character for which stats are being input. 

    Returns: 

    A tuple of (health, attack, defense). 

    """ 

    print(f"\nEnter the stats for {character_name}:") 

    health = int(input("Health: ")) 

    attack = int(input("Attack: ")) 

    defense = int(input("Defense: ")) 

    return health, attack, defense 

  

# Function to compare two characters' stats 

def compare_characters(char1_name, char1_stats, char2_name, char2_stats): 

    """ 

    Compares the stats of two characters and prints the results. 

    Parameters: 

    - char1_name: Name of Character 1 

    - char1_stats: Stats of Character 1 (tuple of health, attack, defense) 

    - char2_name: Name of Character 2 

    - char2_stats: Stats of Character 2 (tuple of health, attack, defense) 

    """ 

    print(f"\nComparing Characters:") 

    print(f"{char1_name}: {char1_stats}") 

    print(f"{char2_name}: {char2_stats}") 

  

    # Compare health 

    if char1_stats[0] > char2_stats[0]: 

        print(f"{char1_name} has more health.") 

    elif char1_stats[0] < char2_stats[0]: 

        print(f"{char2_name} has more health.") 

    else: 

        print("Both characters have the same health.") 

  

    # Compare attack 

    if char1_stats[1] > char2_stats[1]: 

        print(f"{char1_name} has more attack.") 

    elif char1_stats[1] < char2_stats[1]: 

        print(f"{char2_name} has more attack.") 

    else: 

        print("Both characters have the same attack.") 

  

    # Compare defense 

    if char1_stats[2] > char2_stats[2]: 

        print(f"{char1_name} has more defense.") 

    elif char1_stats[2] < char2_stats[2]: 

        print(f"{char2_name} has more defense.") 

    else: 

        print("Both characters have the same defense.") 

  

# Function to display character selection menu 

def character_selection_menu(characters): 

    """ 

    Displays the character selection menu and returns the selected character. 

    Parameters: 

    - characters: List of available characters. 

    Returns: 

    The selected character. 

    """ 

    print("\nCharacter Selection Menu:") 

    for i, character in enumerate(characters, 1): 

        print(f"{i}. {character}") 

  

    while True: 

        selection = int(input("Select a character (1-{}): ".format(len(characters)))) 

        if 1 <= selection <= len(characters): 

            return characters[selection - 1] 

        else: 

            print("Invalid selection. Please choose a valid character.") 

  

# Main function to run the character selection 

def character_selection(): 

    """ 

    Main function to run the character selection process. 

    """ 

    print("Welcome to the Fighting Game Character Selection!\n") 

  

    # Get stats for Character 1 

    char1_name = character_selection_menu(["aiden", "jaiden", "melina", "blaze", "blackmask", "Jack"]) 

    char1_stats = get_character_stats(char1_name) 

  

    # Get stats for Character 2 

    char2_name = character_selection_menu(["aiden", "jaiden", "melina", "blaze", "blackmask", "Jack"]) 

    char2_stats = get_character_stats(char2_name) 

  

    # Compare characters 

    compare_characters(char1_name, char1_stats, char2_name, char2_stats) 

  

# Run the character selection 

character_selection() 

    
    
        
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