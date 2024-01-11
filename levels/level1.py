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
from obstacles.final_flag import FinalFlag
from obstacles.arrow_sign import ArrowSign

from superiors.strawberry import Strawberry
from superiors.apple import Apple
from superiors.cherry import Cherry
from superiors.pineapple import Pineapple

from enemies.fat_bird import FatBird
from enemies.bluebird import BlueBird
from enemies.bunny import Bunny

class Level1():
    
    def reset_level(self):
        block_size = 96
        self.level1 = [Block(i*block_size, HEIGHT - block_size, block_size, block_size,96, 0) for i in range(0, 12)] # WIDTH * 2//block_size
        self.level2 = [Block(i*block_size, HEIGHT + 2*block_size, block_size, block_size,96, 0) for i in range(-7, 18)]
        self.level3 = [Block(i*block_size, HEIGHT, block_size, block_size,96, 0) for i in range(-13, -7)]
        self.floor = [*self.level1, *self.level2, *self.level3]

        self.arrowsign = ArrowSign(100, HEIGHT - 2*block_size - 2*64, 64, 64)
        self.final_flag = FinalFlag(-block_size*8 - 50, HEIGHT - 3*block_size - 2*64, 64, 64)

        
        self.spiked_ball = [SpikedBall(block_size*14 + 40, HEIGHT - block_size * 3 + 100, 28, 28, 200)]
        self.chains = [Chain(block_size*14 + 60, HEIGHT - block_size * 3 + 120, 8, 8, i * 25) for i in range(1, 8)]
        self.floor.append(Block(block_size*14 + 60 - 8, HEIGHT - block_size * 3 + 120 - 10 ,32, 32, 192, 80))

        self.spiked_ball.append(SpikedBall(-338, 700, 28, 28, 200))
        self.chains += [Chain(-318, 720, 8, 8, i * 25) for i in range(1, 8)]
        self.floor.append(Block(-318 - 8, 720 - 10,32, 32, 192, 80))


        self.fire = [Fire(block_size * 13, HEIGHT - block_size * 3 - 64, 16, 32), Fire(-block_size, HEIGHT - block_size * 4 - 64, 16, 32), Fire(-block_size*4, HEIGHT - block_size * 7 - 64, 16, 32)]

        self.saws = [Saw(block_size * 5 - 38, HEIGHT - block_size * 6 - 38, 38, 38, 
                         4*block_size, block_size, 6)] # trasa prostokata

        self.wall1 = [Block(block_size * 18, HEIGHT - i*block_size, block_size, block_size,96, 0) for i in range(-2, 8)] ## NA TYM MAJA BYC OWOCKI
        self.wall2 = [Block(-block_size * 7, HEIGHT - i*block_size, block_size, block_size,96, 0) for i in range(-2, 8)]
        self.wall3 = [Block(0, HEIGHT - block_size * i, block_size, block_size, 96, 0) for i in range(2, 10)]
        self.wall4 = [Block(-block_size*13, HEIGHT - i*block_size, block_size, block_size, 96, 0) for i in range(0, 9)]
        

        self.blocks = [
                    Block(block_size * 4, HEIGHT - block_size * 4, block_size, 12, 272, 16), #1 platforma
                    Block(block_size, HEIGHT - block_size * 2, block_size, 12, 272, 16), #2 platforma

                    Block(block_size*5, HEIGHT - block_size * 6, block_size, block_size, 96, 0),#blocki od piły
                    Block(block_size*6, HEIGHT - block_size * 6, block_size, block_size, 96, 0),
                    Block(block_size*7, HEIGHT - block_size * 6, block_size, block_size, 96, 0),
                    Block(block_size*8, HEIGHT - block_size * 6, block_size, block_size, 96, 0),


                    Block(block_size*13, HEIGHT - block_size * 3, block_size, block_size, 96, 0),
                    Block(block_size*14, HEIGHT - block_size * 3, block_size, block_size, 96, 0),
                    Block(block_size*15, HEIGHT - block_size * 3, block_size, block_size, 96, 0),

                    Block(block_size*12, HEIGHT + block_size, block_size, block_size, 96, 0), #klocki od spikehead
                    Block(0, HEIGHT + block_size, block_size, block_size, 96, 0),
                    *self.wall1,
                    *self.wall2,
                    *self.wall3,
                    *self.wall4,

                    Block(-block_size, HEIGHT -   4*block_size, block_size, block_size, 96, 0), #blocki w wiezyczce
                    Block(-block_size*2, HEIGHT - 4*block_size, block_size, block_size, 96, 0),
                    Block(-block_size*3, HEIGHT - 4*block_size, block_size, block_size, 96, 0),

                    Block(-block_size*6, HEIGHT - 7*block_size, block_size, block_size, 96, 0), #blocki w wiezyczce
                    Block(-block_size*5, HEIGHT - 7*block_size, block_size, block_size, 96, 0),
                    Block(-block_size*4, HEIGHT - 7*block_size, block_size, block_size, 96, 0),

                    Block(-block_size*8, HEIGHT - 6*block_size, block_size, block_size, 96, 0),# blocki po wyjsciu z wiezyczki (fajny kwadracik)
                    Block(-block_size*11, HEIGHT - 7*block_size, block_size, block_size, 96, 0),
                    Block(-block_size*9, HEIGHT - 6*block_size, block_size, block_size, 96, 0),
                    Block(-block_size*8, HEIGHT - 3*block_size, block_size, block_size, 96, 0),
                    Block(-block_size*9, HEIGHT - 3*block_size, block_size, block_size, 96, 0),
                    Block(-block_size*10, HEIGHT - 6*block_size, block_size, block_size, 96, 0),
                    Block(-block_size*11, HEIGHT - 6*block_size, block_size, block_size, 96, 0),
                    Block(-block_size*11, HEIGHT - 5*block_size, block_size, block_size, 96, 0),
                    Block(-block_size*11, HEIGHT - 4*block_size, block_size, block_size, 96, 0),
                    Block(-block_size*11, HEIGHT - 3*block_size, block_size, block_size, 96, 0),

                    Block(-block_size - 10, HEIGHT - 10, block_size, 12, 272, 16), #3 platforma
                    Block(-6*block_size + 10, HEIGHT - 10 - block_size*2, block_size, 12, 272, 16), #4 platforma

        ]
        
        self.spikes = [Spikes(i*16, HEIGHT - block_size - 2*16, 16, 16) for i in range(6, 68)]
        self.spikes += [Spikes(-block_size * 10 + i*16, HEIGHT - 6*block_size - 2*16, 16, 16) for i in range(0, 16)]

        FallingPlatform(block_size * 2.5, HEIGHT - block_size * 3, 32, 10)
        FallingPlatform(block_size * 10, HEIGHT - block_size * 3, 32, 10)
        FallingPlatform(block_size * 11, HEIGHT - block_size * 3, 32, 10)
        FallingPlatform(-block_size * 9, HEIGHT - block_size * 7 - 50, 32, 10)
        


        ### KONCOWE DODANIE ELEMENTOW DO LIST
        self.objects = [*self.floor, *self.blocks, *self.fire, *self.spiked_ball, *self.spikes, self.final_flag]
        self.objects_notcoll = [self.arrowsign, *self.chains]



        ### SUPERIORS
        [Strawberry(5*block_size - 40 + i*40, HEIGHT - 7*block_size, 32, 32) for i in range (1,10)]
        [Strawberry(5*block_size - 20 + i*40, HEIGHT - 7*block_size - 50, 32, 32) for i in range (1,10)]
        [Strawberry(60+ i * 50, HEIGHT + block_size, 32, 32) for i in range (1,21)]
        Apple(-318 - 22, 720 - 65, 32, 32)
        [Cherry(block_size * 17 , HEIGHT - i*50, 32, 32) for i in range (1,8)]
        [Cherry(block_size * 16 + 50, HEIGHT - i*50, 32, 32) for i in range (1,8)]
        [Cherry(-block_size*12 + 20, HEIGHT - i*50, 32, 32) for i in range (2,14)]
        Pineapple(-5*block_size - 80, HEIGHT - 10 - block_size*2 - 60, 32, 32)
        
        self.superiors = Apple.all_apples
        self.superiors.add(Strawberry.all_strawberries, Cherry.all_cherries, Pineapple.all_pineapples)

        
        ### INTERACT ELEMENTS
        self.spikehead = SpikeHead(block_size * 8, HEIGHT + block_size - 14, 54, 52, self.blocks)

        self.interact_elements = pygame.sprite.Group()
        self.interact_elements.add(FallingPlatform.all_falling_platforms, self.spikehead, SpikeHead(-block_size * 11, HEIGHT - block_size - 14, 54, 52, self.blocks))




        ### ENEMIES
        FatBird(block_size * 16 + 60, HEIGHT + 16, 40, 48, self.floor, 400)
        FatBird(-block_size - 82, HEIGHT - block_size * 4 - 64, 40, 48, self.objects, 250)
        
        self.enemies = pygame.sprite.Group()
        self.enemies.add(FatBird.all_fatbirds)
    
    def clear_map(self):
        self.objects = []
        self.objects_notcoll = []
        for sup in self.superiors:
            sup.kill()
        for elem in self.interact_elements:
            elem.kill()
        for enemy in self.enemies:
            enemy.kill()
