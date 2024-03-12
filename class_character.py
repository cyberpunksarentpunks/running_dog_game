# For all Player or NPC characters
# - icon is image of a character
# - posX / posY is a default spawning point for that character
# - posX/Y_change is difference between a current position and moving into other direction
# - health is a health :D
# - weapon = if a character pick some weapon or already has any(for enemies), the type of weapon should be passed as a string here. Default value is 'none'
# - weapon_ammo = how much "bullets" for that weapon a character has.
# - weapon_action = Default state value is "still". When a character fires, it changes to "fire"
# - score = score :D
# - running = ...

class Character:
    def __init__(self, icon, posX, posY, posX_change, posY_change, health, weapon, weapon_ammo, weapon_action, score, running):
        self.icon = icon
        self.x = posX
        self.y = posY
        self.x_change = posX_change
        self.y_change = posY_change
        self.hp = health
        self.wp = weapon
        self.wp_ammo = weapon_ammo
        self.wp_action = weapon_action
        self.score = score
        self.running = True
    
    # Draws a scaled and transparent png image of character into X,Y position on the screen 
    def draw_character(self, image_path, image_size):
        import pygame
        from main import screen
        image = pygame.image.load(image_path).convert_alpha()
        character_scale = pygame.transform.scale(image, image_size)
        character_icon = screen.blit(character_scale, (self.x,self.y))
        return character_icon 
    
    #@staticmethod  <- I don't know if that should be there!
    # function that detects a collision between the given points
    def is_collision(self, characterX,characterY,objectX,objectY, target_distance): # optimal value = 40
        import math
        distance = math.sqrt(math.pow(characterX - objectX, 2) + (math.pow(characterY - objectY, 2)))
        if distance < target_distance:
            return True
        else:
            return False
    

    # setting up how the player1 moves and all his input as attack etc
    def player_move(self):
        import pygame
        from main import bone
        # quiting the game when a quit button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.x_change
            print("Left arrow is pressed")
        if keys[pygame.K_RIGHT]:
            self.x += self.x_change
            print("Right arrow is pressed")
        if keys[pygame.K_SPACE]:
            self.wp_action = "fire"
            # if self.wp_action == "fire":
            #     bone.bone_shoot(self.x, self.y)    
            #     print("shoot")
            #     if bone.y < 0:
            #         self.wp_action = "ready"
        if keys[pygame.K_ESCAPE]:
            print("Game has been canceled")
            self.running = False
    
    
        
    
    # Creating borders of map for player that he cannot pass
    def check_borders(self):
        if self.x <= 0:
            self.x = 0
        elif self.x >= 1100:
            self.x = 1100

    # 
    def player_attacked(self):
        print("Hit")
        


# -------------------------------------------------------------------------------        
# Enemies has same attributes but can perform different actions

class Enemy(Character):
    def __init__(self, icon, posX, posY, posX_change, posY_change, health, weapon, weapon_ammo, weapon_action, score, running=True):
        super().__init__(icon, posX, posY, posX_change, posY_change, health, weapon, weapon_ammo, weapon_action, score, running)


    # enemies are moving down and eventually respawn back to the top after touching the ground border
    def enemy_move(self):
        import random
        from main import HEIGHT, WIDTH
        self.y += self.y_change
        # If the enemy reaches the bottom of the screen, reset its position
        if self.y > HEIGHT:
            self.y = random.randint(-200, 0)
            self.x = random.randint(0, WIDTH)
    

    
    
        
    