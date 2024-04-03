import sys, random, pygame
#final project, jahreem jeffers, V0.0

resolution = 0# 0 = Low Resolution, 2 = High Reslution

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080
screen = pygame.display.set_mode((x, y))

pygame.init()

difficulty = int(input("Please choose a difficulty. Enter 1 for EASY or 2 for HARD.\n"))

if difficulty == 1:
    pygame.display.set_caption('jackblack -- SIMPO')
else:
    pygame.display.set_caption('jackblack -- XFACTOR')

# Define card values
card_values = {'1': 1, '2': 2, '3':3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Define a class for a deck of cards
class Deck:
    def __init__(self):
        self.cards = list(card_values.keys()) * 4 # 4 decks of cards
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()

# Define a class for the players hand
class Hand:
    def __init__(self):
        self.cards + []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

print(card_values)









YOURMOM = 255, 255, 255