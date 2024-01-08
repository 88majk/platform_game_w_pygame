import pygame
from graphic_setup import load_sprite_sheets
from object import Object

class Apple(Object):
    ANIMATION_DELAY = 2
    all_apples = pygame.sprite.Group()

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "apple")
        self.apple = load_sprite_sheets("Items", "Fruits", width, height)
        self.image = self.apple["Apple"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.collect_animation_count = 0
        self.collection_pic = load_sprite_sheets("Items", "Fruits", width, height)
        self.image_col = self.collection_pic["Collected"][0]
        self.collected = False
        Apple.all_apples.add(self)

    
    def loop(self):
        sprites = self.apple["Apple"]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)

        if self.collected:
            self.image = self.get_collect_animation_frame()
            self.collect_animation_count += 1
            
            if self.collect_animation_count > 10:
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

