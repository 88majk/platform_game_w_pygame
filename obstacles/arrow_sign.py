import pygame
from graphic_setup import load_sprite_sheets
from object import Object

class ArrowSign(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "start_platform")
        self.start_platform = load_sprite_sheets("Items", r"Checkpoints\Start", width, height)
        self.image = self.start_platform["Start (Moving) (64x64)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.collect_animation_count = 0
        self.animation_name = "Start (Moving) (64x64)"
        
    
    def loop(self):
        sprites = self.start_platform[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)

        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.amimation_count = 0