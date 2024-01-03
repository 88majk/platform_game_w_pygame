import pygame
from graphic_setup import load_sprite_sheets
import math
from object import Object

class Chain(Object):
    ANIMATION_DELAY = 3
    acceleration = 0.4

    def __init__(self, x, y, width, height, r):
        super().__init__(x, y, width, height, "chain")
        self.chain = load_sprite_sheets("Traps", "Spiked Ball", width, height)
        self.image = self.chain["Chain"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_name = "Chain"
        self.x = x
        self.y = y
        self.radius = r
        self.angle = 10
        self.speed = 5
    
    def loop(self):
        acceleration_x = self.acceleration * math.cos(math.radians(self.angle))
        acceleration_y = self.acceleration * math.sin(math.radians(self.angle))

        # Zaktualizuj prędkość z uwzględnieniem przyspieszenia i oporu powietrza
        self.speed += acceleration_x
        

        # Oblicz nowe współrzędne na podstawie prędkości
        self.rect.x = self.x + int(self.radius * math.cos(math.radians(self.angle)))
        self.rect.y = self.y + int(self.radius * math.sin(math.radians(self.angle)))

        # Zaktualizuj kąt, aby obiekt obracał się wokół okręgu
        self.angle += self.speed

        sprites = self.chain[self.animation_name]
        self.image = sprites[0]

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))