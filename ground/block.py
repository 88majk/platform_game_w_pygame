import pygame
from os.path import isfile, join
from object import Object

def load_block(size, size2, choice1, choice2):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size2), pygame.SRCALPHA, 32)
    rect = pygame.Rect(choice1, choice2, size, size2)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface) 

class Block(Object):
    def __init__(self, x, y, size, size2, choice1, choice2):
        super().__init__(x, y, size, size2)
        block = load_block(size, size2, choice1, choice2)
        self.image.blit(block, (0,0))
        self.mask = pygame.mask.from_surface(self.image)

    def loop(self):
        pass 