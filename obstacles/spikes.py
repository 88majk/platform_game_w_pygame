import pygame
from graphic_setup import load_sprite_sheets
from object import Object

class Spikes(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "spikes")
        self.spike = load_sprite_sheets("Traps", "Spikes", width, height)
        self.image = self.spike["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_name = "Idle"
    
    def loop(self):
        sprites = self.spike[self.animation_name]
        self.image = sprites[0]

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)