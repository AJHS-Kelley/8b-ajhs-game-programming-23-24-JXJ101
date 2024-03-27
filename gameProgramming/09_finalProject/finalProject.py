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






