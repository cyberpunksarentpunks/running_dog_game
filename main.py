import math
import pygame
from pygame.locals import *
import random
from class_bullet import *
from class_item import *
from class_character import *
import sys
import score_function
from score_function import display_highscores

# initialize the pygame
pygame.init()

# writing to the test file
test_file = "test.txt"

# creating the screen
WIDTH = 1200
HEIGHT = 800
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors for menu
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# caption(title) and icon
pygame.display.set_caption("Running Dog")
icon = pygame.image.load("img/icon.png").convert()
pygame.display.set_icon(icon)
bg_map = pygame.image.load("img/bg_map.jpg").convert()
bg_size = (1024, 800)
bg_set = pygame.transform.scale(bg_map, bg_size)


# Character and object creations
player = Character(icon="dog.png", posX=200, posY=600, posX_change=15, posY_change=0, health=1, weapon="none", weapon_ammo="none", weapon_action="none", score=0, running=True)
cat1 = Enemy(icon="cat.png", posX=400, posY=100, posX_change=0, posY_change=2.5, health=1, weapon="none", weapon_ammo="none", weapon_action="none", score=None, running=True)
cat2 = Enemy(icon="cat.png", posX=100, posY=100, posX_change=0, posY_change=2.5, health=1, weapon="none", weapon_ammo="none", weapon_action="none", score=None, running=True)

bone = Bullet(image="img/bone.png", image_size=(40,50), bullet_state="ready", damage=1, speed=10, posX=player.x, posY=player.y, X_change=0, Y_change=5)


enemies_list = (cat1, cat2)


# ------------------------------------------------------
# _menu_loop_
# Fonts for buttons
font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 48)

# Create menu buttons
play_button = pygame.Rect(WIDTH // 2 - 100, 200, 200, 50)
highscore_button = pygame.Rect(WIDTH // 2 - 100, 300, 200, 50)
quit_button = pygame.Rect(WIDTH // 2 - 100, 400, 200, 50)

def menu_image():
    image_load = pygame.image.load("img/menu_image.jpeg")
    image_scale = pygame.transform.scale(image_load, (WIDTH, HEIGHT))
    proc_image = screen.blit(image_scale, (0, 0))
    return proc_image

# This loop will display menu
def menu_loop():
    running = True
    while running:
        
        menu_image()
        
        # Draw buttons
        pygame.draw.rect(screen, BLACK, play_button)
        pygame.draw.rect(screen, BLACK, highscore_button)
        pygame.draw.rect(screen, BLACK, quit_button)

        # Draw button text
        play_text = button_font.render("Play", True, WHITE)
        screen.blit(play_text, (play_button.x + 70, play_button.y + 15))

        highscore_text = button_font.render("Highscore", True, WHITE)
        screen.blit(highscore_text, (highscore_button.x + 25, highscore_button.y + 15))

        quit_text = button_font.render("Quit", True, WHITE)
        screen.blit(quit_text, (quit_button.x + 70, quit_button.y + 15))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = event.pos
                    if play_button.collidepoint(mouse_pos):
                        print("Play button clicked!")
                        singleplayer_game_loop()
                    elif highscore_button.collidepoint(mouse_pos):
                        print("Highscore button clicked!")
                        display_highscores()
                    elif quit_button.collidepoint(mouse_pos):
                        print("Quit button clicked!")
                        running = False
                        pygame.quit()

                        

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)


# --------------------------------------------------------------
# This should start when "Singleplayer/Play button is clicked"
# _game_loop_
def singleplayer_game_loop():
    running = True
    while running:
        
        screen.fill((0, 100, 60))
        screen.blit(bg_map, (-1080,-900))
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            print("Game has been canceled")
            running = False
            menu_loop()
        
        # <- ALL OF THIS IS CREATING INFINITE RECURSION -> NEEDS TO BE SOLVED  !!!!
        # if player.wp_action == "fire":
            # bone.bone_shoot(player.x, player.y)
            # for each_enemy in enemies_list:
            #     hit = player.is_collision(each_enemy.x, each_enemy.y, bone.x, bone.y, 40)
            #     if hit:
            #         player.player_attacked()  
                     
        
        player.draw_character("img/dog.png", (100,100))
        cat1.draw_character("img/cat.png", (80,100))
        cat2.draw_character("img/cat.png", (80,100))
         
        player.player_move()
        player.check_borders()
        
            
        cat1.enemy_move()
        cat2.enemy_move()
        

                                   
        pygame.display.update()
    
    
# MAIN PROGRAM LOOP
running = True
while running:
    menu_loop()
    singleplayer_game_loop()

pygame.quit()
sys.exit()


