import pygame
from graphic_setup import *
from collisions import *
from object import Object
from player import Player
from ground.block import Block
from ground.falling_platform import FallingPlatform
from obstacles.fire import Fire
from obstacles.spikes import Spikes
from obstacles.saw import Saw
from obstacles.spike_head import SpikeHead
from superiors.strawberry import Strawberry
from superiors.apple import Apple
from obstacles.final_flag import FinalFlag

class Level1():
    
    def reset_level(self):
        block_size = 96
        self.level1 = [Block(i*block_size, HEIGHT - block_size, block_size, 96, 0) for i in range(-13, 15)] # WIDTH * 2//block_size
        self.level2 = [Block(i*block_size, HEIGHT + 2*block_size, block_size, 96, 0) for i in range(-WIDTH // block_size, WIDTH * 2//block_size)]
        self.floor = [*self.level1, *self.level2]

        self.final_flag = FinalFlag(1000, HEIGHT - block_size - 2*64, 64, 64)

        [FallingPlatform(i*100, HEIGHT - block_size - 4*16, 32, 10) for i in range(1, 10)]


        self.fire = []

        self.saws = [Saw(block_size * 5 - 38, HEIGHT - block_size * 6 - 38, 38, 38, 
                         4*block_size, block_size)] # trasa prostokata


        self.blocks = [Block(block_size * 3, HEIGHT - block_size * 4, block_size, 96, 0), 
                       Block(block_size * 3, HEIGHT + block_size , block_size, 96, 0), 
                       Block(block_size * 15, HEIGHT + block_size , block_size, 96, 0), 
                       Block(0, HEIGHT - block_size * 2, block_size, 96, 0),
                       Block(0, HEIGHT - block_size * 3, block_size, 96, 0),
                       Block(block_size * 5, HEIGHT - block_size * 6, block_size, 96, 0),
                       Block(block_size * 6, HEIGHT - block_size * 6, block_size, 96, 0),
                       Block(block_size * 7, HEIGHT - block_size * 6, block_size, 96, 0),
                       Block(block_size * 8, HEIGHT - block_size * 6, block_size, 96, 0)]
        
        self.spikes = [Spikes(i*100, HEIGHT - block_size - 2*16, 16, 16) for i in range(1, 8)]



        ### SUPERIORS
        [Strawberry(i*50, HEIGHT - 5*block_size, 32, 32) for i in range (1,11)]
        [Apple(i*(-100), HEIGHT - 2*block_size, 32, 32) for i in range (1,3)]
        

        ### KONCOWE DODANIE ELEMENTOW DO LIST
        self.objects = [*self.floor, *self.saws, *self.blocks, *self.fire, *self.spikes, self.final_flag]
        
        self.superiors = Apple.all_apples
        self.superiors.add(Strawberry.all_strawberries)
        

        self.spikehead = SpikeHead(block_size * 3, HEIGHT - 2*block_size - 54, 54, 52, self.objects)
        self.interact_elements = pygame.sprite.Group()
        self.interact_elements.add(FallingPlatform.all_falling_platforms, self.spikehead)
    
    def clear_map(self):
        self.objects = []
        # INNE CZYSZCZENIE NIE DZIALA (NIE WIEM CZEMU NA OBECNA CHWILE)
        for sup in self.superiors:
            sup.kill()
        for elem in self.interact_elements:
            elem.kill()
