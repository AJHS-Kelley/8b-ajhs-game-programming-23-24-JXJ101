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
clock = pygame.time.Clock()
game_active = True

difficulty = int(input("Please choose a difficulty. Enter 1 for EASY or 2 for HARD.\n"))

if difficulty == 1:
    pygame.display.set_caption('jackblack -- SIMPO')
else:
    pygame.display.set_caption('jackblack -- LV3XFACTOR')


test_font = pygame.font.Font(None, 50)

game_name = test_font.render('JXJ blackjack', False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400, 80))


background = pygame.image.load('img/ultply/background3.PNG').convert_alpha()
background = pygame.transform.rotozoom(background,0,2)

game_name = test_font.render('JXJ BlackJack', False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Press space to play',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,300))


# Define card values
card_values = {'2': 2, '3':3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

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
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value +=  card_values[card]
        if card == 'A':
            self.value += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Define a function for taking a player's input

def take_player_input():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h: 
                    return 'h'

                

                    print(card_values)
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()



    if game_active:
        screen.blit(background, (0,0))
    pygame.display.update()
    clock.tick(60)
