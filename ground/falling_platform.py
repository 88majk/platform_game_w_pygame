import pygame
from graphic_setup import load_sprite_sheets
from object import Object
import math
import random

class FallingPlatform(Object):
    ANIMATION_DELAY = 3
    all_falling_platforms = pygame.sprite.Group()
    linspace = 1

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "falling_platforms")
        self.falling_platform = load_sprite_sheets("Traps", "Falling Platforms", width, height)
        self.image = self.falling_platform["On (32x10)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_name = "On (32x10)"
        self.animation_count = 0
        self.jumpedOn = False
        self.fall_speed = 0
        self.linspace = random.randint(1, 20)
        self.original_y = y  # Dodaj oryginalną pozycję Y, aby odtworzyć unoszenie
        FallingPlatform.all_falling_platforms.add(self)
    
    def loop(self):
        sprites = self.falling_platform[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        
        self.linspace += 2
        if not self.jumpedOn:
            displacement = 20 * math.sin(self.linspace / 20)  
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.original_y + displacement))
        else:
            self.fall_speed += 1.3
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y + self.fall_speed))
        
        if self.rect.y > 1300:
            self.jumpedOn = False
            self.kill()
        
        if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.animation_count = 0
