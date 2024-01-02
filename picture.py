import pygame

class Picture():
    def __init__(self, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        

    def draw(self, window, x, y):
        window.blit(self.image, (x, y))