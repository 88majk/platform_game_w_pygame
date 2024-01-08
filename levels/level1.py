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
from obstacles.spiked_ball import SpikedBall
from obstacles.chain import Chain
from superiors.strawberry import Strawberry
from superiors.apple import Apple
from obstacles.final_flag import FinalFlag
from obstacles.arrow_sign import ArrowSign

from enemies.fat_bird import FatBird

class Level1():
    
    def reset_level(self):
        block_size = 96
        self.level1 = [Block(i*block_size, HEIGHT - block_size, block_size, 96, 0) for i in range(-3, 15)] # WIDTH * 2//block_size
        self.level2 = [Block(i*block_size, HEIGHT + 2*block_size, block_size, 96, 0) for i in range(-WIDTH // block_size, WIDTH * 2//block_size)]
        self.floor = [*self.level1, *self.level2]

        self.start_platform = ArrowSign(100, HEIGHT - block_size - 2*64, 64, 64)
        self.final_flag = FinalFlag(1000, HEIGHT - block_size - 2*64, 64, 64)

        
        self.spiked_ball = SpikedBall(-628, 600, 28, 28, 200)
        self.chains = [Chain(-608, 620, 8, 8, i * 25) for i in range(1, 8)]

        [FallingPlatform(i*100, HEIGHT - block_size - 4*16, 32, 10) for i in range(1, 10)]


        self.fire = []

        self.saws = [Saw(block_size * 5 - 38, HEIGHT - block_size * 6 - 38, 38, 38, 
                         4*block_size, block_size)] # trasa prostokata


        self.blocks = [Block(block_size * 3, HEIGHT - block_size * 4, block_size, 96, 0),
                       
                       Block(block_size * 3, HEIGHT + block_size , block_size, 96, 0), 
                       Block(block_size * 15, HEIGHT + block_size , block_size, 96, 0), 
                       Block(0, HEIGHT - block_size * 2, block_size, 96, 0),
                       Block(0, HEIGHT - block_size * 3, block_size, 96, 0),
                       Block(0, HEIGHT - block_size * 4, block_size, 96, 0),
                       Block(block_size * 5, HEIGHT - block_size * 6, block_size, 96, 0),
                       Block(block_size * 6, HEIGHT - block_size * 6, block_size, 96, 0),
                       Block(block_size * 7, HEIGHT - block_size * 6, block_size, 96, 0),
                       Block(block_size * 8, HEIGHT - block_size * 6, block_size, 96, 0),
                       Block(-614, 600, 32, 192, 80)]
        
        self.spikes = [Spikes(i*100, HEIGHT - block_size - 2*16, 16, 16) for i in range(1, 8)]



        ### SUPERIORS
        [Strawberry(i*50, HEIGHT - 5*block_size, 32, 32) for i in range (1,11)]
        [Apple(i*(-100), HEIGHT - 2*block_size, 32, 32) for i in range (1,3)]
        

        ### KONCOWE DODANIE ELEMENTOW DO LIST
        self.objects = [*self.floor, *self.saws, *self.blocks, *self.fire, self.final_flag, self.spiked_ball]
        self.objects_notcoll = [self.start_platform, *self.chains]
        
        self.superiors = Apple.all_apples
        self.superiors.add(Strawberry.all_strawberries)
        

        self.spikehead = SpikeHead(block_size * 8, HEIGHT + block_size - 14, 54, 52, self.blocks)

        self.interact_elements = pygame.sprite.Group()
        #self.interact_elements.add(FallingPlatform.all_falling_platforms, self.spikehead)

        FatBird(-100, HEIGHT - 2*block_size + 16, 40, 48, self.objects, 400)
        self.enemies = FatBird.all_fatbirds
    
    def clear_map(self):
        self.objects = []
        self.objects_notcoll = []
        self.enemies = []
        # INNE CZYSZCZENIE NIE DZIALA (NIE WIEM CZEMU NA OBECNA CHWILE)
        for sup in self.superiors:
            sup.kill()
        for elem in self.interact_elements:
            elem.kill()
