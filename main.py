# ----source - freecodeacademy YT pygame
import pygame
from pygame.locals import *

# initialize the pygame
pygame.init()

# creating the screen
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# caption(title) and icon
pygame.display.set_caption("Running Dog")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

# player - img, size, position
player_origin_img = pygame.image.load("img/dog.png")
player_size = (100, 100)
player_icon = pygame.transform.scale(player_origin_img, player_size)
playerX = 550
playerY = 650

# enemy - img, size
enemy_origin_img = pygame.image.load("img/cat.png")
enemy_size = (80, 100)
enemy_icon = pygame.transform.scale(enemy_origin_img, enemy_size)
enemyX = 100
enemyY = 200

def player():
    screen.blit(player_icon, (playerX,playerY))

def enemy():
    screen.blit(enemy_icon, (enemyX, enemyY))

# _game loop_
running = True
while running:

    screen.fill((0, 100, 60))
    # quiting the game when a quit button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    enemy()
    pygame.display.update()




































































































