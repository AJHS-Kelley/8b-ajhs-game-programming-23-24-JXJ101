import sys
import random
import pygame
import os
#final project, jahreem jeffers, V0.0

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("JXJ's Blackjack")

resolution = 0# 0 = Low Resolution, 2 = High Reslution

background = pygame.image.load('img/ultply/background3.PNG').convert_alpha()
background = pygame.transform.rotozoom(background,0,2)

test_font = pygame.font.Font(None, 50)

game_name = test_font.render('JXJ blackjack', False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400, 80))

#def load_card_images():
    #cards = {}
    #suits = ['diamonds', 'club', 'hearts', 'spades']
    #for suit in suits:
        #for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            #filename = os.path.join("PNG", f"card_{value}.png")
            #cards[value] = pygame.image.load(filename)
    #return cards


# Load card images
#card_images = load_card_images()
#card_image = pygame.image.load('img/ultply/PNG')
pygame.display.set_caption('JXJ black jack')


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

#difficulty = int(input("Please choose a difficulty. Enter 1 for EASY or 2 for HARD.\n"))

#if difficulty == 1:
    #pygame.display.set_caption('jackblack -- SIMPO')
#else:
    #pygame.display.set_caption('jackblack -- LV3XFACTOR')
#game_message = test_font.render('Press space to play',False,(111,196,169))
#game_message_rect = game_message.get_rect(center = (400,300))


# Define card values
card_images = {}
#for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
    #for rank in range(1, 14):
        #card_images[(suit, rank)] = pygame.image.load(f'img/ultply/PNG/Cards_(Large)/card_{suit}_{rank}.png')


# Define a class for a deck of cards
class Deck:
    def __init__(self):
        self.cards = list(card_images.keys()) * 4 # 4 decks of cards
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
        self.value +=  card_images[card]
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
                elif event.key == pygame.K_s:
                    return's'
        pygame.event.pump()

# define a function to display cards 
def display_cards(player_name, player, dealer, show_dealer_card=False):
    #Clear the screen
    screen.fill((0, 128, 0))
    
    # Disply player's hand
    for i, card in enumerate(player.cards):
        screen.blit(card_images[card], (100 + i * 120, screen - 300))

    # Display dealer's hand
    if  show_dealer_card:
        for i, card in enumerate(player.cards):
            screen.blit(card_images[card], (100 + i * 120, screen - 500))
    else:
        screen.blit(card_images['2'], (100, screen - 500))

    pygame.display.flip()


# Define a function to check if the player has won or not and if possible tied
def determine_outcome(player_name, player, dealer, bet):
    if player.value > 21:
        print("Player busts! Dealer wins!")
        return -bet
    elif dealer.value > 21:
        print("Dealer busts! {} wins!".format(player_name))
        return bet * 2 
    elif player.value == dealer.value:
        print("luckily Its a tie")
        return 0
    elif player.value > dealer.value:
        print("{} wins!".format(player_name))
    else:
        print("Dealer wins!")
        return -bet

# where the real stuff to play the game
def play_blackjack():
    player_name = input(f"Enter your name plz: ")
    money = 100 # the amount of money you start with
    while True:
        print("\n{}'s Money: ${}".format(player_name, money))
        bet = int(input("place your bet: $"))
        if bet > money: 
            print("pick the amount you have broke boi.")
            continue

        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        dealer_hand = Hand()

    # deal
        for _ in range(2):
            player_hand.add_card(deck.deal_card())
            dealer_hand.add_card(deck.deal_card())
        display_cards(player_name, player_hand, dealer_hand)

    # Player's turn
        while True:
            choice = take_player_input()
            if choice == 'h':
                player_hand.add_card(deck.deal_card())
                player_hand.adjustfor_ace()
                display_cards(player_name, player_hand, dealer_hand)
                if player_hand.value > 21:
                    money += determine_outcome(player_name, player_hand, dealer_hand, bet)
                    break
            else:
                break

        while dealer_hand.value < 17:
            dealer_hand.add_card(deck.deal_card())
            dealer_hand.adjust_for_ace()

        display_cards(player_name, player_hand, dealer_hand, show_dealer_card= True)
    
        money += determine_outcome(player_name, player_hand, dealer_hand, bet)

        if money <= 0:
            print("hope you like being a hobo bro. Game over")
            break

        choice = input("Do you want to keep going and double down> (yes/no): ").lower()
        if choice != 'yes':
            print("Thanks for playing! Final money: ${}".format(money))
            break

    play_blackjack()

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
