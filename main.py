import math
import pygame
from pygame.locals import *
import random

from class_enemy import *

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
player_lives = 1
player_gun = False

# enemy - img, size
# enemy_origin_img = []
# enemy_X = []
# enemyY = []
# enemyX_change = []
# enemyY_change = []
# num_of_enemies = 6

enemy_icon = pygame.transform.scale(pygame.image.load("img/cat.png"), (80,100))
cat1 = Enemy(icon=enemy_icon,enemyX=random.randint(0, 1100),enemyY=random.randint(-300,50),enemyX_change=0,enemyY_change=1)
cat2 = Enemy(icon=enemy_icon,enemyX=random.randint(0, 1100),enemyY=random.randint(-300,50),enemyX_change=0,enemyY_change=1)
cat3 = Enemy(icon=enemy_icon,enemyX=random.randint(0, 1100),enemyY=random.randint(-300,50),enemyX_change=0,enemyY_change=1)
cat4 = Enemy(icon=enemy_icon,enemyX=random.randint(0, 1100),enemyY=random.randint(-300,50),enemyX_change=0,enemyY_change=1)
cat5 = Enemy(icon=enemy_icon,enemyX=random.randint(0, 1100),enemyY=random.randint(-300,50),enemyX_change=0,enemyY_change=1)
cat6 = Enemy(icon=enemy_icon,enemyX=random.randint(0, 1100),enemyY=random.randint(-300,50),enemyX_change=0,enemyY_change=1)



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

food_origin_img = pygame.image.load("img/food.png")
food_size  = (60,60)
food_icon = pygame.transform.scale(food_origin_img, food_size)
foodX = random.randint(0, 1100)
foodY = -1000
foodY_change = 1
foodX_change = 0

gun_origin_img = pygame.image.load("img/gun.png")
gun_size = (70,70)
gun_icon = pygame.transform.scale(gun_origin_img, gun_size)
gunX = random.randint(0, 1100)
gunY = - 500
gunX_change = 0
gunY_change = 1
gun_state = "ready"
gun_ammo = 5

drop_origin_img = pygame.image.load("img/drop.png")
drop_size = (90,90)
drop_icon = pygame.transform.scale(drop_origin_img, drop_size)
dropX = 0
dropY = 650
dropX_change = 0
dropY_change = 3
drop_state = "ready"

bottle_origin_img = pygame.image.load("img/bottle.png")
bottle_size = (60,60)
bottle_icon = pygame.transform.scale(bottle_origin_img, bottle_size)
bottleX = 0
bottleY = 650
bottleX_change = 0
bottleY_change = 1
bottle_full = 5

score = 0

def player(x, y):
    screen.blit(player_icon, (x, y))

def enemy(x, y):
    screen.blit(cat1.icon, (x, y))

def food_spawn(x, y):
    screen.blit(food_icon, (x, y))
    
def gun_spawn(x, y):
    screen.blit(gun_icon, (x,y))

def bottle_spawn(x, y):
    screen.blit(bottle_icon, (x,y))

def fire_bone(x, y):
    global bone_state
    bone_state = "fire"
    screen.blit(bone_icon, (x+32, y+20))

def fire_water(x, y):
    global drop_state
    drop_state = "fire"
    screen.blit(drop_icon, (x,y))
    
def is_collision(enemyX,enemyY,boneX,boneY):
    distance = math.sqrt(math.pow(enemyX-boneX,2) + (math.pow(enemyY-boneY,2)))
    if distance < 40:
        return True
    else:
        return False

#---------------------------------------------------------
def player_collision(enemyX,enemyY,playerX,playerY):
    distance = math.sqrt(math.pow(enemyX-playerX,2) + (math.pow(enemyY-playerY,2)))
    if distance < 65:
        return True
    else:
        return False
def food_collision(foodX,foodY,playerX,playerY):
    distance = math.sqrt(math.pow(foodX-playerX,2) + (math.pow(foodY-playerY,2)))
    if distance < 65:
        return True
    else:
        return False
def gun_collision(gunX,gunY,playerX,playerY):
    distance = math.sqrt(math.pow(gunX-playerX,2) + (math.pow(gunY-playerY,2)))
    if distance < 65:
        return True
    else:
        return False
def bottle_collision(bottleX,bottleY,playerX,playerY):
    distance = math.sqrt(math.pow(bottleX-playerX,2) + (math.pow(bottleY-playerY,2)))
    if distance < 65:
        return True
    else:
        return False
# --------------------------------------------------------------
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
                print("Space is pressed")
                bone_state = "fire"
                boneX = playerX
                fire_bone(boneX, boneY)
                print(bone_state)
                
            if event.key == pygame.K_LCTRL:
                if gun_ammo != 0:      
                    print("LCtrl is pressed")
                    gun_state = "fire"
                    dropX = playerX
                    gunX = playerX
                    fire_water(dropX, dropY)
                else:
                    gun_state = "ready"

            if event.key == pygame.K_ESCAPE:
                print("Game has been canceled")
                running = False
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key has been released")
                playerX_change = 0
            if event.key == pygame.K_SPACE:
                print("Backspace has been released")
                #bone_state = "ready"
                

    # moving across axis            
    playerX += playerX_change
    cat1.y += cat1.y_change
    cat2.y += cat2.y_change
    cat3.y += cat3.y_change
    cat4.y += cat4.y_change
    cat5.y += cat5.y_change
    cat6.y += cat6.y_change
    foodY += foodY_change
    gunY += gunY_change
    bottleY += bottleY_change
    
    #boneX = playerX
    # boneY = playerY
        
    
    if gun_state == "fire":
        fire_water(dropX,dropY)
        dropY -= dropY_change
        gun_ammo -= 1
        if dropY < 0:       # checks if a water drop reached the top
            dropY = 650
            gun_state = "ready"

    # bone fire movement
    if bone_state == "fire":
        fire_bone(boneX, boneY)
        boneY -= boneY_change
        if boneY < 0:       # checks if a bone reached the top
            boneY = 650
            bone_state = "ready"

    # ------collision between CAT and BONE/bullets-------------
    collisionW1 = is_collision(cat1.x,cat1.y,dropX,dropY)
    if collisionW1:
        dropY = 650
        drop_state = "ready"
        score += 1
        print(f"You hit the cat. Score is {score}")
        cat1.x = random.randint(0, 1100)
        cat1.y = random.randint(-300,50)
    collisionW2 = is_collision(cat2.x,cat2.y,dropX,dropY)
    if collisionW2:
        dropY = 650
        drop_state = "ready"
        score += 1
        print(f"You hit the cat. Score is {score}")
        cat2.x = random.randint(0, 1100)
        cat2.y = random.randint(-300,50)
    collisionW3 = is_collision(cat3.x,cat3.y,dropX,dropY)
    if collisionW3:
        dropY = 650
        drop_state = "ready"
        score += 1
        print(f"You hit the cat. Score is {score}")
        cat3.x = random.randint(0, 1100)
        cat3.y = random.randint(-300,50)
    collisionW4 = is_collision(cat4.x,cat4.y,dropX,dropY)
    if collisionW4:
        dropY = 650
        drop_state = "ready"
        score += 1
        print(f"You hit the cat. Score is {score}")
        cat4.x = random.randint(0, 1100)
        cat4.y = random.randint(-300,50)
    collisionW5 = is_collision(cat5.x,cat5.y,dropX,dropY)
    if collisionW5:
        dropY = 650
        drop_state = "ready"
        score += 1
        print(f"You hit the cat. Score is {score}")
        cat5.x = random.randint(0, 1100)
        cat5.y = random.randint(-300,50)
    collisionW6 = is_collision(cat6.x,cat6.y,dropX,dropY)
    if collisionW6:
        dropY = 650
        drop_state = "ready"
        score += 1
        print(f"You hit the cat. Score is {score}")
        cat6.x = random.randint(0, 1100)
        cat6.y = random.randint(-300,50)    
    
    collision = is_collision(cat1.x,cat1.y,boneX,boneY)
    if collision:
        boneY = 650
        bone_state = "ready"
        score += 1
        print(f"You hit the cat. Score is {score}")
        cat1.x = random.randint(0, 1100)
        cat1.y = random.randint(-300,50)
    collision2 = is_collision(cat2.x,cat2.y,boneX,boneY)
    if collision2:
        boneY = 650
        bone_state = "ready"
        score += 1
        print(f"You hit the cat. Score is {score}")
        cat2.x = random.randint(0, 1100)
        cat2.y = random.randint(-300,50)
    collision3 = is_collision(cat3.x,cat3.y,boneX,boneY)
    if collision3:
        boneY = 650
        bone_state = "ready"
        score += 1
        print(f"You hit the cat. Score is {score}")
        cat3.x = random.randint(0, 1100)
        cat3.y = random.randint(-300,50)
    collision4 = is_collision(cat4.x,cat4.y,boneX,boneY)
    if collision4:
        boneY = 650
        bone_state = "ready"
        score += 1
        print(f"You hit the cat. Score is {score}")
        cat4.x = random.randint(0, 1100)
        cat4.y = random.randint(-300,50)
    collision5 = is_collision(cat5.x,cat5.y,boneX,boneY)
    if collision5:
        boneY = 650
        bone_state = "ready"
        score += 1
        print(f"You hit the cat. Score is {score}")
        cat5.x = random.randint(0, 1100)
        cat5.y = random.randint(-300,50)
    collision6 = is_collision(cat6.x,cat6.y,boneX,boneY)
    if collision6:
        boneY = 650
        bone_state = "ready"
        score += 1
        print(f"You hit the cat. Score is {score}")
        cat6.x = random.randint(0, 1100)
        cat6.y = random.randint(-300,50)
        
    # ----------- Collision between player and CAT-------------------    
    p_collision1 = player_collision(cat1.x,cat1.y,playerX,playerY)
    if p_collision1:
        player_lives -= 1
        cat1.x = random.randint(0,1100)
        cat1.y = random.randint(-300,50)
        print("Cat took 1 life from you")
        if player_lives == 0:
            running = False
    p_collision2 = player_collision(cat2.x,cat2.y,playerX,playerY)
    if p_collision2:
        player_lives -= 1
        cat2.x = random.randint(0,1100)
        cat2.y = random.randint(-300,50)
        print("Cat took 1 life from you")
        if player_lives == 0:
            running = False
    p_collision3 = player_collision(cat3.x,cat3.y,playerX,playerY)
    if p_collision3:
        player_lives -= 1
        cat3.x = random.randint(0,1100)
        cat3.y = random.randint(-300,50)
        print("Cat took 1 life from you")
        if player_lives == 0:
            running = False
    p_collision4 = player_collision(cat4.x,cat4.y,playerX,playerY)
    if p_collision4:
        player_lives -= 1
        cat4.x = random.randint(0,1100)
        cat4.y = random.randint(-300,50)
        print("Cat took 1 life from you")
        if player_lives == 0:
            running = False
    p_collision5 = player_collision(cat5.x,cat5.y,playerX,playerY)
    if p_collision5:
        player_lives -= 1
        cat5.x = random.randint(0,1100)
        cat5.y = random.randint(-300,50)
        print("Cat took 1 life from you")
        if player_lives == 0:
            running = False
    p_collision6 = player_collision(cat6.x,cat6.y,playerX,playerY)
    if p_collision6:
        player_lives -= 1
        cat6.x = random.randint(0,1100)
        cat6.y = random.randint(-300,50)
        print("Cat took 1 life from you")
        if player_lives == 0:
            running = False
    #-------------------Food, bottle and Gun collision-------------------------------------------
    f_collision = food_collision(foodX,foodY,playerX,playerY)
    if f_collision:
        player_lives += 1
        foodX = random.randint(0,1100)
        foodY = random.randint(-1000,-10)
        print("You gained +1 health")
        
    g_collision = gun_collision(gunX,gunY,playerX,playerY)
    if g_collision:
        gunX = random.randint(0,1100)
        gunY = random.randint(-5000,-2000)
        player_gun = True
        print("You found a water gun")  
    
    b_collision = bottle_collision(bottleX,bottleY,playerX,playerY)
    if b_collision:
        bottleX = random.randint(0,1100)
        bottleY = random.randint(-1000,-50)
        gun_ammo += bottle_full
        print("You found a water bottle")     
            
    # Creating borders of map
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1100:
        playerX = 1100

   
    player(playerX, playerY)
    enemy(cat1.x, cat1.y)
    enemy(cat2.x,cat2.y)
    enemy(cat3.x,cat3.y)
    enemy(cat4.x,cat4.y)
    enemy(cat5.x,cat5.y)
    enemy(cat6.x,cat6.y)
    food_spawn(foodX, foodY)
    gun_spawn(gunX,gunY)
    bottle_spawn(bottleX, bottleY)
    
    if player_gun:
        screen.blit(gun_icon, (playerX + 10,playerY+35))

    
    # respawning enemy after they cross down line
    if cat1.y == 800:
        print("enemy goes to end")
        cat1.y = 0
        cat1.x = random.randint(0, 1100)
    if cat2.y == 800:
        print("enemy goes to end")
        cat2.y = 0
        cat2.x = random.randint(0, 1100)
    if cat3.y == 800:
        print("enemy goes to end")
        cat3.y = -30
        cat3.x = random.randint(0, 1100)
    if cat4.y == 800:
        print("enemy goes to end")
        cat4.y = -50
        cat4.x = random.randint(0, 1100)
    if cat5.y == 800:
        print("enemy goes to end")
        cat5.y = -50
        cat5.x = random.randint(0, 1100)
    if cat6.y == 800:
        print("enemy goes to end")
        cat6.y = -50
        cat6.x = random.randint(0, 1100)
    # if enemy2Y == 800:
    #     print("enemy2 goes to end")
    #     enemy2Y = -100
    #     enemy2X = random.randint(0, 1100)
    if foodY == 800:
        print("Food has been respawned")
        foodY = -100
        foodX = random.randint(0, 1100)
    if gunY == 800:
        print("Gun has been respawned")
        gunY = -100
        gunX = random.randint(0, 1100)
    if bottleY == 800:
        print("Bottle has been respawned")
        bottleY = -100
        bottleX = random.randint(0, 1100)
        
    pygame.display.update()
