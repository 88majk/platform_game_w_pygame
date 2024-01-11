import pygame
from graphic_setup import load_sprite_sheets
from object import Object

class Banana(Object):
    ANIMATION_DELAY = 2
    all_bananas = pygame.sprite.Group()

    def __init__(self, x, y, width = 32, height = 32, name=None):
        super().__init__(x, y, width, height, "banana")
        self.Banana = load_sprite_sheets("Items", "Fruits", width, height)
        self.image = self.Banana["Bananas"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        ### ANIMACJE ZBIERANIA
        self.collect_animation_count = 0
        self.collection_pic = load_sprite_sheets("Items", "Fruits", width, height)
        self.image_col = self.collection_pic["Collected"][0]
        self.collected = False
        Banana.all_bananas.add(self)

    def loop(self):
        sprites = self.Banana["Bananas"]
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
        self.mask = pygame.mask.from_surface(self.image)


    def get_collect_animation_frame(self):
        collect_sprites = self.collection_pic["Collected"]
        frame_index = (self.collect_animation_count // 2) % len(collect_sprites)
        return collect_sprites[frame_index]
