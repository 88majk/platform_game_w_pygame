import pygame
from graphic_setup import load_sprite_sheets
from object import Object

class FallingPlatform(Object):
    ANIMATION_DELAY = 3
    all_falling_platforms = pygame.sprite.Group()

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "falling_platforms")
        self.falling_platform = load_sprite_sheets("Traps", "Falling Platforms", width, height)
        self.image = self.falling_platform["On (32x10)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_name = "On (32x10)"
        self.animation_count = 0
        self.jumpedOn = False
        FallingPlatform.all_falling_platforms.add(self)
    
    def loop(self):
        sprites = self.falling_platform[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        if not self.jumpedOn:
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        else:
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y + 7))
        if self.rect.y > 900:
                self.jumpedOn = False
                FallingPlatform.all_falling_platforms.remove(self)
                

        if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.animation_count = 0
        