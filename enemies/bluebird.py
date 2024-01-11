import pygame
from graphic_setup import load_sprite_sheets
from object import Object

class BlueBird(Object):
    ANIMATION_DELAY = 3
    GRAVITY = 1
    all_bluebirds = pygame.sprite.Group()

    def __init__(self, x, y, width, height, fly_lenght):
        super().__init__(x, y, width, height, "blue_bird")
        self.blue_bird = load_sprite_sheets("Enemies", "BlueBird", width, height)
        self.image = self.blue_bird["Flying (32x32)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_name = "Flying (32x32)"
        self.animation_count = 0
        self.hit_animation_count = 0
        self.direction = -1
        self.x_vel = 3
        self.org_x = x
        self.killed = False
        self.jumpedOn = False
        self.active = True
        self.fly_lenght = fly_lenght
        self.fall_vel = 0
        BlueBird.all_bluebirds.add(self)

    def loop(self):
        if not self.jumpedOn:
            if self.direction == 1:
                sprites = self.flip(self.blue_bird[self.animation_name])
            else:
                sprites = self.blue_bird[self.animation_name]
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            self.image = sprites[sprite_index]
            if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
                self.animation_count = 0

    
        self.animation_count += 1

        if self.rect.x > self.org_x + self.fly_lenght:
            self.direction *= -1
        elif self.rect.x < self.org_x - self.fly_lenght:
            self.direction *= -1
        self.rect.x += self.direction * self.x_vel

        if self.jumpedOn:
            self.image = self.get_animation_frame("Hit (32x32)")
            self.hit_animation_count += 1
            if self.hit_animation_count > 14:
                self.hit_animation_count = 0
                self.killed = True

        if self.killed:
            self.rect.y += self.fall_vel
            self.fall_vel += self.GRAVITY
            if self.rect.y > 1300:
                self.kill()

        


    def get_animation_frame(self, animation_name):
        sprites = self.blue_bird[animation_name]
        frame_index = (self.hit_animation_count // 4) % len(sprites)
        return sprites[frame_index]
    
    def flip(self, sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]
