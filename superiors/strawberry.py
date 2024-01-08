import pygame
from graphic_setup import load_sprite_sheets
from object import Object

class Strawberry(Object):
    ANIMATION_DELAY = 2
    all_strawberries = pygame.sprite.Group()

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "strawberry")
        self.strawberry = load_sprite_sheets("Items", "Fruits", width, height)
        self.image = self.strawberry["Strawberry"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        ### ANIMACJA ZBIERANIA
        self.collect_animation_count = 0
        self.collection_pic = load_sprite_sheets("Items", "Fruits", width, height)
        self.image_col = self.collection_pic["Collected"][0]
        self.collected = False
        Strawberry.all_strawberries.add(self)

    
    def loop(self):
        sprites = self.strawberry["Strawberry"]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)

        if self.collected:
            self.image = self.get_collect_animation_frame()
            self.collect_animation_count += 1
            
            if self.collect_animation_count > 12:
                self.collect_animation_count = 0
                self.kill()
        else:
            self.image = sprites[sprite_index]
            self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
    
    def get_collect_animation_frame(self):
        collect_sprites = self.collection_pic["Collected"]
        frame_index = (self.collect_animation_count // 2) % len(collect_sprites)
        return collect_sprites[frame_index]

