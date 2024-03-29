import pygame
from graphic_setup import load_sprite_sheets
import time

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 4
    
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height, name):
        super().__init__()
        self.SPRITES = load_sprite_sheets("MainCharacters", name, 32, 32, True)
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.score = 0
        self.life_points = 3
        self.hit_count = 0
        self.bug_protect = True
        self.wall_jump = False
        ### timery
        self.gravity_multiplier = 1
        self.gravity_reduction_start_time = 0  
        self.gravity_reduction_duration = 10
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.wall_jump = False
        self.x_vel = -vel
        if self.direction != "left":
            self.animation_count = 0

    def move_right(self, vel):
        self.wall_jump = False
        self.x_vel = vel
        if self.direction != "right":
            self.animation_count = 0

    def jump(self):
        self.wall_jump = False
        self.y_vel = -self.GRAVITY * 4
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)
        self.fall_count += 1
        
        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps:
            self.hit = False
            self.life_points -= 1
            self.hit_count = 0
            self.bug_protect = True
        self.update_sprite()

        ### timery
        if self.gravity_multiplier < 1 and time.time() - self.gravity_reduction_start_time > self.gravity_reduction_duration:
            self.gravity_multiplier = 1  

        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY / self.gravity_multiplier)


    def make_hit(self):
        if self.bug_protect:
            self.hit = True
            self.hit_count = 0
            self.bug_protect = False
    
    def collect_points(self, points):
        self.score += points
    
    def collect_apple(self):
        if self.life_points < 4:
            self.life_points += 1

    def landed(self):
        self.wall_jump = False
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0
    
    def slide(self, dy=0):
        if self.y_vel > 0.9 or self.y_vel < -0.9:
            self.wall_jump = True
            self.y_vel = dy/3
            self.jump_count = 0
    
    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def win(self):
        self.score  += 100*self.life_points
        

    def update_sprite(self):
        sprite_sheet = "idle"
        if self.hit:
            sprite_sheet = "hit"

        if self.wall_jump:
            sprite_sheet = "wall_jump"

        if self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.udpate()

    def udpate(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, window, offset_x, offset_y):
        window.blit(self.sprite, (self.rect.x - offset_x, self.rect.y - offset_y))
    
    def start_gravity_reduction(self):
        self.gravity_multiplier = 0.001  # Ustaw mnożnik grawitacji na niższą wartość
        self.gravity_reduction_start_time = time.time()

