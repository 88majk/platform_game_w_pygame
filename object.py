import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name= None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.name = name

    def draw(self, window, offset_x, offset_y):
        window.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))
    
    def loop(self):
        pass