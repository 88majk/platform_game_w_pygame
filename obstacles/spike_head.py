import pygame
from graphic_setup import load_sprite_sheets
from object import Object

class SpikeHead(Object):
    ANIMATION_DELAY = 9
    MAX_SPEED = 12  # Maksymalna prędkość przeszkody
    ACCELERATION = 0.2  # Wartość przyspieszenia
    DECELERATION = 1.0  # Wartość spowolnienia

    def __init__(self, x, y, width, height, objects):
        super().__init__(x, y, width, height, "spike_head")
        self.spikeHead = load_sprite_sheets("Traps", "Spike Head", width, height)
        self.image = self.spikeHead["Blink (54x52)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Blink (54x52)"

        ### ANIMACJA ZDERZENIA
        self.hit_animation_count = 0
        # self.hit_animation_name = "Left Hit (54x52)"
        # self.image = self.spikeHead["Left Hit (54x52)"][0]
        self.L_hit = False
        self.R_hit = False
        self.current_speed = self.MAX_SPEED 

        self.objects = objects
        self.direction = -1  # Kierunek ruchu: 1 - w prawo, -1 - w lewo

    def loop(self):
        sprites = self.spikeHead[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        

        self.rect.x += self.direction * self.current_speed

        collisions = pygame.sprite.spritecollide(self, self.objects, False)
        for block in collisions:
            if self.direction == 1:
                if block in collisions:
                    self.direction *= -1
                    self.rect.right = block.rect.left 
                    collisions.pop(collisions.index(block))
                    self.R_hit = True
                    self.current_speed = 0
            if self.direction == -1:
                if block in collisions:
                    self.direction *= -1 
                    self.rect.left = block.rect.right 
                    collisions.pop(collisions.index(block))
                    self.L_hit = True
                    self.current_speed = 0

        if self.L_hit:
            self.image = self.get_hit_animation_frame("Left Hit (54x52)")
            self.hit_animation_count += 1
            if self.hit_animation_count > 12:
                self.hit_animation_count = 0
                self.L_hit = False
        elif self.R_hit:
            self.image = self.get_hit_animation_frame("Right Hit (54x52)")
            self.hit_animation_count += 1
            if self.hit_animation_count > 12:
                self.hit_animation_count = 0
                self.R_hit = False
        else:
            self.image = sprites[sprite_index]
            self.animation_count += 1

        if not self.L_hit and not self.R_hit:
            self.current_speed += self.ACCELERATION
            if self.current_speed > self.MAX_SPEED:
                self.current_speed = self.MAX_SPEED

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
    
    def get_hit_animation_frame(self, animation_name):
        collect_sprites = self.spikeHead[animation_name]
        frame_index = (self.hit_animation_count // 4) % len(collect_sprites)
        return collect_sprites[frame_index]
