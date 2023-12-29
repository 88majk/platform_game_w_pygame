import pygame
from graphic_setup import load_sprite_sheets
from object import Object

class Strawberry(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "Strawberry")
        self.strawberry = load_sprite_sheets("Items", "Fruits", width, height)
        self.image = self.strawberry["Strawberry"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.collection_pic = load_sprite_sheets("Items", "Fruits", width, height)
        self.image_col = self.collection_pic["Collected"][0]
        self.mask_col = pygame.mask.from_surface(self.image_col)
    
    def loop(self):
        sprites = self.strawberry["Strawberry"]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.amimation_count = 0
    
    def collected(self):
        sprites = self.collection_pic["Collected"]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.collect_img = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image_col.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask_col = pygame.mask.from_surface(self.collect_img)

        