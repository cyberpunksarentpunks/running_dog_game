

# bone/bullet -ready state- cannot be seem
#             -fire state - bone is currently moving

class Bullet:
    
    def __init__(self, image, image_size, bullet_state, damage, speed, posX, posY, X_change=0, Y_change=0):
        self.img = image
        self.img_size = image_size
        self.state = bullet_state
        self.dmg = damage
        self.speed = speed
        self.x = posX
        self.y = posY
        self.X_change = X_change
        self.Y_change = Y_change
        
    # Function that checks if a player can shoot and if he do, then it will draw a bullet image
    def bone_shoot(self, playerX, playerY):
        import pygame
        from main import screen     
        self.bone_shoot(playerX, playerY)
        load_image = pygame.image.load("img/bone.png")
        image_scaled = pygame.transform.scale(load_image, (40,50))
        
        if self.state == "ready":
                self.x = playerX + 30  # Set bullet starting position to player's x
                self.y = playerY  # Set bullet starting position to player's y
                self.state = "fire"

        # Update bullet position and draw it into the screen
        if self.state == "fire":
            shoot = screen.blit(image_scaled, (self.x,self.y))
            self.y -= self.speed
            # Check if the bullet goes off the screen
            if self.y < 0:
                self.state = "ready"
        return shoot
    
        
        
        
        
