import pygame

class Item:
    
    def __init__(self, image, image_size, item_state, magazine, damage, speed, posX, posY, X_change=0, Y_change=0,):
        self.img = image
        self.img_size = image_size
        self.state = item_state
        self.mag = magazine
        self.dmg = damage
        self.speed = speed
        self.x = posX
        self.y = posY
        self.X_change = X_change
        self.Y_change = Y_change
        
        
        
    def draw_item(self, image_path, image_size):
        from main import screen
        image = pygame.image.load(image_path).convert_alpha()
        item_scale = pygame.transform.scale(image, image_size)
        item_icon = screen.blit(item_scale, (self.x,self.y))
        return item_icon
    