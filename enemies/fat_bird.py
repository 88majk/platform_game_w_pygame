import pygame
from graphic_setup import load_sprite_sheets
from object import Object
import random

class FatBird(Object):
    ANIMATION_DELAY = 3
    GRAVITY = 1
    all_fatbirds = pygame.sprite.Group()
    def __init__(self, x, y, width, height, objects, flight_height):
        super().__init__(x, y, width, height, "fat_bird")
        self.fat_bird = load_sprite_sheets("Enemies", "FatBird", width, height)
        self.image = self.fat_bird["Idle (40x48)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_name = "Idle (40x48)"
        self.animation_count = 0
        self.fall_animation_count = 0
        self.flightPeek = False
        self.killed = False
        self.test = False
        self.bugProtect = True
        self.fall_speed = 0
        self.flight_height = flight_height
        self.displacement = 0
        self.flight_vel = 1.5
        self.original_y = y  
        self.objects = objects
        FatBird.all_fatbirds.add(self)
    
    def loop(self):
        sprites = self.fat_bird[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        
        collisions = pygame.sprite.spritecollide(self, self.objects, False)

        if not self.killed:
            for block in collisions:
                    if block in collisions:
                        self.rect.bottom = block.rect.top
                        collisions.pop(collisions.index(block))
                        self.flightPeek = False
                        self.fall_speed = 0  

        if self.test and not self.killed:
                self.image = self.get_animation_frame("Hit (40x48)")
                self.fall_animation_count += 1
                if self.fall_animation_count > 14:
                    self.fall_animation_count = 0
                    self.killed = True
                    self.test = False
        elif not self.flightPeek and not self.killed:
            self.animation_name = "Idle (40x48)"
            self.displacement -= self.flight_vel
            self.image = sprites[sprite_index]
            self.animation_count += 1
            # Unoszenie
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.original_y + self.displacement))

            if self.displacement < -self.flight_height:
                self.displacement = 0
                self.flightPeek = True
                         
        elif self.flightPeek and not self.killed:
            self.animation_name = "Fall (40x48)"
            self.fall_speed += self.GRAVITY
            self.rect.y += self.fall_speed
            self.image = sprites[sprite_index]
            self.animation_count += 1
        
        elif self.killed:
            self.fall_speed += self.GRAVITY
            self.rect.y += self.fall_speed
            if self.rect.y > 1300:
                self.kill()
        
        if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.animation_count = 0
    

    def get_animation_frame(self, animation_name):
        collect_sprites = self.fat_bird[animation_name]
        frame_index = (self.fall_animation_count // 4) % len(collect_sprites)
        return collect_sprites[frame_index]
