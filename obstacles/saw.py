import pygame
from graphic_setup import load_sprite_sheets
from object import Object

class Saw(Object):
    ANIMATION_DELAY = 3
    all_saws = pygame.sprite.Group()

    def __init__(self, x, y, width, height, trip_x, trip_y):
        super().__init__(x, y, width, height, "saw")
        self.saw = load_sprite_sheets("Traps", "Saw", width, height)
        self.image = self.saw["on"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_name = "on"
        self.animation_count = 0
        self.x = x
        self.y = y
        self.trip_x = trip_x
        self.trip_y = trip_y
        self.direction_x = 1  
        self.direction_y = 0  
        self.saw_vel = 6
        Saw.all_saws.add(self)
    
    def loop(self):
        sprites = self.saw[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        
        
        if self.direction_x == 1: ## RUCH PO X W PRAWO
            self.rect.x += self.saw_vel
            if self.rect.x < self.x or self.rect.x > self.x + self.trip_x:
                self.direction_x = 0  
                self.direction_y = 1  

        
        if self.direction_y == 1: ## RUCH PO Y W DOL
            self.rect.y += self.saw_vel
            if self.rect.y < self.y or self.rect.y > self.y + self.trip_y:
                self.direction_y = 0  
                self.direction_x = -1
        

        if self.direction_x == -1: ## RUCH PO X W LEWO
            self.rect.x -= self.saw_vel
            if self.rect.x < self.x or self.rect.x > self.x + self.trip_x :
                self.direction_x = 0  
                self.direction_y = -1  


        if self.direction_y == -1: ## RUCH PO Y W GORE
            self.rect.y -= self.saw_vel
            if self.rect.y < self.y or self.rect.y > self.y + self.trip_y:
                self.direction_y = 0  
                self.direction_x = 1
        

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

        if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.animation_count = 0
