import pygame
from graphic_setup import load_sprite_sheets
from object import Object

class Bunny(Object):
    ANIMATION_DELAY = 3
    GRAVITY = 1
    all_bunnies = pygame.sprite.Group()

    def __init__(self, x, y, width, height, run_lenght, direction):
        super().__init__(x, y, width, height, "bunny")
        self.bunny = load_sprite_sheets("Enemies", "Bunny", width, height)
        self.image = self.bunny["Run (34x44)"][0]
        self.mask = pygame.sprite.from_surface(self.image)
        self.animation_name = "Run (34x44)"
        self.animation_count = 0
        self.hit_animation_count = 0
        self.direction = direction
        self.x_vel = 2
        self.org_x = x
        self.killed = False
        self.jumpedOn = False
        self.active = True
        self.run_lenght = run_lenght
        self.fall_vel = 0
        Bunny.all_bunnies.add(self)

    def loop(self):
        if not self.jumpedOn:
            if self.direction == 1:
                sprites = self.flip(self.bunny[self.animation_name])
            else:
                sprites = self.bunny[self.animation_name]
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            self.image = sprites[sprite_index]
            self.animation_count += 1

            if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
                self.animation_count = 0

        if self.rect.x > self.org_x + self.run_lenght:
            self.direction *= -1
        elif self.rect.x < self.org_x - self.run_lenght:
            self.direction *= -1

        self.rect.x += self.direction * self.x_vel

        if self.jumpedOn:
            self.image = self.get_animation_frame("Hit (34x44)")
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
        sprites = self.bunny[animation_name]
        frame_index = (self.hit_animation_count // 4) % len(sprites)
        return sprites[frame_index]

    def flip(self, sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]