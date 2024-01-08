import pygame
from graphic_setup import load_sprite_sheets
from object import Object

class FinalFlag(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "final_flag")
        self.final_flag = load_sprite_sheets("Items", r"Checkpoints\Checkpoint", width, height)
        self.image = self.final_flag["Final Flag (Idle)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.collect_animation_count = 0
        self.animation_name = "Final Flag (Idle)"
        self.collected = False
        self.lvl_end = False
        
    
    def loop(self):
        sprites = self.final_flag[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)

        if self.collected:
            self.image = self.get_collect_animation_frame()
            self.collect_animation_count += 1

            if self.collect_animation_count > 52:
                self.image = self.final_flag["Checkpoint (No Flag)"][0]
                self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
                self.lvl_end = True
        else:
            self.image = sprites[sprite_index]
            self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.amimation_count = 0
    
    def get_collect_animation_frame(self):
        collect_sprites = self.final_flag["Checkpoint (Flag Out) (64x64)"]
        frame_index = len(collect_sprites) - ((self.collect_animation_count // 2) % len(collect_sprites)) -1
        return collect_sprites[frame_index]
