import pygame
from pygame.locals import *
import random
import math
from enemies import *

# initialize the pygame
pygame.init()

# creating the screen
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# caption(title) and icon
pygame.display.set_caption("Running Dog")
icon = pygame.image.load("img/icon.png").convert()
pygame.display.set_icon(icon)
bg_map = pygame.image.load("img/bg_map.jpg").convert()
bg_size = (1024, 800)
bg_set = pygame.transform.scale(bg_map, bg_size)

# player - img, size, position
player_origin_img = pygame.image.load("img/dog.png")
player_size = (100, 100)
player_icon = pygame.transform.scale(player_origin_img, player_size)
playerX = 550
playerY = 650
playerX_change = 0

# enemy - img, size
# enemy_origin_img = []
# enemy_X = []
# enemyY = []
# enemyX_change = []
# enemyY_change = []
# num_of_enemies = 6


enemy_origin_img = pygame.image.load("img/cat.png")
enemy_size = (80, 100)
enemy_icon = pygame.transform.scale(enemy_origin_img, enemy_size)
enemyX = random.randint(0, 1100)
enemyY = random.randint(-300,50)
enemyY_change = 1


# bone/bullet -ready state- cannot be seem
#             -fire state - bone is currently moving
bone_origin_img = pygame.image.load("img/bone.png")
bone_size = (40, 50)
bone_icon = pygame.transform.scale(bone_origin_img, bone_size)
boneX = 0
boneY = 650
boneX_change = 0
boneY_change = 3
bone_state = "ready"

score = 0

def player(x, y):
    screen.blit(player_icon, (x, y))

def enemy(x, y):
    screen.blit(enemy_icon, (x, y))

def fire_bone(x, y):
    global bone_state
    bone_state = "fire"
    screen.blit(bone_icon, (x+32, y+20))
    
def is_collision(enemyX,enemyY,boneX,boneY):
    distance = math.sqrt(math.pow(enemyX-boneX,2) + (math.pow(enemyY-boneY,2)))
    if distance < 40:
        return True
    else:
        return False
    
# _game loop_
running = True
while running:

    screen.fill((0, 100, 60))
    screen.blit(bg_map, (-1080,-900))
    # quiting the game when a quit button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # if key stroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
                print("Right arrow is pressed")

            if event.key == pygame.K_SPACE:
                print("Backspace is pressed")
                bone_state = "fire"
                boneX = playerX
                fire_bone(boneX, boneY)
                print(bone_state)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key has been released")
                playerX_change = 0
            if event.key == pygame.K_SPACE:
                print("Backspace has been released")
                #bone_state = "ready"
                

    # moving across axis            
    playerX += playerX_change
    enemyY += enemyY_change
    
    boneX = playerX
    # boneY = playerY

    # bone fire movement
    if bone_state == "fire":
        fire_bone(boneX, boneY)
        boneY -= boneY_change
        if boneY < 0:       # checks if a bone reached the top
            boneY = 650
            bone_state = "ready"

    # collision
    collision = is_collision(enemyX,enemyY,boneX,boneY)
    if collision:
        boneY = 650
        bone_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 1100)
        enemyY = random.randint(-300,50)


    # Creating borders of map
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1100:
        playerX = 1100

    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    
    # respawning enemy after they cross down line
    if enemyY == 800:
        print("enemy goes to end")
        enemyY = 0
        enemyX = random.randint(0, 1100)
    # if enemy2Y == 800:
    #     print("enemy2 goes to end")
    #     enemy2Y = -100
    #     enemy2X = random.randint(0, 1100)

    pygame.display.update()



































































































