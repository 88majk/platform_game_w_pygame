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
from superiors.banana import Banana

from enemies.fat_bird import FatBird
from enemies.bluebird import BlueBird
from enemies.bunny import Bunny


class Level2():
    
    def reset_level(self):
        block_size = 96
        # Tutaj zaczynają się nowe elementy
        self.level1 = [Block(i*block_size, HEIGHT - block_size, block_size, block_size, 96, 128) for i in range(-1, 12)]
        self.level2 = [Block(i*block_size, HEIGHT - 4*block_size, block_size, block_size, 96, 128) for i in range(9, 18)]
        self.level3 = [Block(i*block_size, HEIGHT - 8*block_size, block_size, block_size, 96, 128) for i in range(3, 17)]
        self.level4 = [Block(i*block_size, HEIGHT - 7*block_size, block_size, block_size, 96, 128) for i in range(23, 31)]
        self.level5 = [Block(i*block_size, HEIGHT - 4*block_size, block_size, block_size, 96, 128) for i in range(28, 39)]
        self.level6 = [Block(i*block_size, HEIGHT + 2*block_size, block_size, block_size, 96, 128) for i in range(12, 19)]
        self.level7 = [Block(i*block_size, HEIGHT + 4*block_size, block_size, block_size, 96, 128) for i in range(2, 12)]
        self.level8 = [Block(i*block_size, HEIGHT + 6*block_size, block_size, block_size, 96, 128) for i in range(-2, 2)]
        self.level9 = [Block(i*block_size, HEIGHT + 6*block_size, block_size, block_size, 96, 128) for i in range(-8, -3)]
        self.floors = [*self.level1, *self.level2, *self.level3, *self.level4, *self.level5, 
                       *self.level6, *self.level7, *self.level8, *self.level9]

        FallingPlatform(block_size * 22, HEIGHT, 32, 10)
        FallingPlatform(block_size * 17.5, HEIGHT - block_size * 8, 32, 10)
        FallingPlatform(block_size * 18.5, HEIGHT - block_size * 7, 32, 10)
        FallingPlatform(block_size * 7 + 40, HEIGHT - block_size * 2 - 48, 32, 10)

        self.saws = [Saw(23*block_size - 38, HEIGHT - 7*block_size - 38, 38, 38, 
                         8*block_size, block_size, 8),
                    Saw(28*block_size - 38, HEIGHT - 4*block_size - 38, 38, 38, 
                         11*block_size, block_size, 10),
                    Saw(-2*block_size - 38, HEIGHT + 6*block_size - 38, 38, 38, 
                         4*block_size, block_size, 7),
                    Saw(-8*block_size - 38, HEIGHT + 6*block_size - 38, 38, 38, 
                         5*block_size, block_size, 9)] 
        
        self.arrowsign = ArrowSign(-block_size, HEIGHT - block_size - 2*64, 64, 64)
        self.final_flag = FinalFlag(block_size * -18 - 38, HEIGHT + 5*block_size - 2*64, 64, 64)

        # # Nowe przeszkody i przeciwnicy
        self.spikes = [Spikes(25*block_size + i*16 - 40, HEIGHT - 7*block_size - 2*16, 16, 16) for i in range(1, 9)]
        self.spikes += [Spikes(25*block_size + i*16 - 40, HEIGHT - 7*block_size - 2*16, 16, 16) for i in range(20, 29)]
        self.spikes += [Spikes(10*block_size + i*16 - 50, HEIGHT - block_size - 2*16, 16, 16) for i in range(1, 12)]

        self.spikes += [Spikes(11*block_size + i*16 - 40, HEIGHT - 4*block_size - 2*16, 16, 16) for i in range(1, 8)]
        self.spikes += [Spikes(12*block_size + i*16 - 40, HEIGHT - 4*block_size - 2*16, 16, 16) for i in range(19, 27)]
        
        self.fire = [Fire(block_size * 18 - 30, HEIGHT - block_size * 4 - 64, 16, 32), 
                     Fire(block_size * 12 - 30, HEIGHT - block_size - 64, 16, 32)]


        self.spiked_ball = []
        self.chains = []
        # self.spiked_ball.append(SpikedBall(-338, 700, 28, 28, 200))
        # self.chains += [Chain(-318, 720, 8, 8, i * 25) for i in range(1, 8)]
        # self.floors.append(Block(-318 - 8, 720 - 10,32, 32, 192, 80))

        self.spiked_ball.append(SpikedBall(block_size * 17 - 20, HEIGHT - 100 - 20, 28, 28, 200))
        self.chains += [Chain(block_size * 17, HEIGHT - 100, 8, 8, i * 25) for i in range(1, 8)]
        self.floors.append(Block(block_size * 17 - 8, HEIGHT - 100 - 10,32, 32, 192, 80))

        self.spiked_ball.append(SpikedBall(block_size * 10 - 20, HEIGHT + block_size - 40 - 20, 28, 28, 200))
        self.chains += [Chain(block_size * 10, HEIGHT + block_size - 40, 8, 8, i * 25) for i in range(1, 8)]
        self.floors.append(Block(block_size * 10 - 8, HEIGHT + block_size - 40 - 10,32, 32, 192, 80))


        # # Nowe owoce
        [Strawberry(5*block_size + 40 + i*60, HEIGHT - 9*block_size, 32, 32) for i in range(-3, 17)]
        [Strawberry(5*block_size + 60 + i*60, HEIGHT - 9*block_size - 50, 32, 32) for i in range(-3, 7)]
        [Strawberry(5*block_size + 60 + i*60, HEIGHT - 9*block_size - 50, 32, 32) for i in range(8, 16)]
        Apple(5*block_size + 60 + 7*60, HEIGHT - 9*block_size - 50, 32, 32)
        [Strawberry(5*block_size + 40 + i*60, HEIGHT - 9*block_size - 100, 32, 32) for i in range(-3, 17)]
        [Cherry(block_size * 23 + i * 60, HEIGHT - 7*block_size - 120, 32, 32) for i in range(1, 11)]
        [Cherry(block_size * 31 + i * 70, HEIGHT - 4*block_size - 70, 32, 32) for i in range(1, 10)]
        [Cherry(block_size * 31 + i * 70 + 20, HEIGHT - 4*block_size - 120, 32, 32) for i in range(1, 9)]
        [Cherry(block_size * 31 + i * 70, HEIGHT - 4*block_size - 170, 32, 32) for i in range(1, 10)]
        [Banana(block_size + i*70, HEIGHT - 2*block_size, 32, 32) for i in range(-1, 9)]
        [Banana(block_size + i*70 + 30, HEIGHT - 2*block_size - 70, 32, 32) for i in range(-1, 8)]
        [Banana(block_size + i*70, HEIGHT - 2*block_size - 140, 32, 32) for i in range(-1, 9)]
        # [Cherry(-block_size*12 + 20, HEIGHT - i*50, 32, 32) for i in range(2, 14)]
        # [Pineapple(i*(100), HEIGHT - 3*block_size, 32, 32) for i in range(1, 8)]

        # Pozostałe elementy mapy pozostają bez zmian
        self.blocks = [
                    Block(block_size * 19, HEIGHT - block_size * 5, block_size, 12, 272, 0), #1 platforma
                    Block(block_size * 21, HEIGHT - block_size * 6, block_size, 12, 272, 0), #2 platforma

                    Block(block_size * 26, HEIGHT - block_size * 2, block_size, 12, 272, 0), #3 platforma
                    Block(block_size * 24, HEIGHT - block_size, block_size, 12, 272, 0), #4 platforma
                    Block(block_size * 20, HEIGHT + block_size, block_size, 12, 272, 0), #5 platforma
                    Block(block_size * -9, HEIGHT + 5*block_size, block_size, 12, 272, 0), #6 platforma
                    Block(block_size * -11, HEIGHT + 4*block_size, block_size, 12, 272, 0), #7 platforma
                    Block(block_size * -13, HEIGHT + 5*block_size, block_size, 12, 272, 0), #8 platforma
                    Block(block_size * -16 - 42, HEIGHT + 5*block_size, block_size, 12, 272, 0), #8 platforma
                    Block(block_size * -18 - 42, HEIGHT + 5*block_size, 128, 96, 272, 128), #zlota platforma

        ]

        self.objects = [*self.spiked_ball, *self.saws, *self.floors, *self.blocks, *self.spikes, *self.fire, self.final_flag]
        self.objects_notcoll = [*self.chains, self.arrowsign]


        self.superiors = Apple.all_apples
        self.superiors.add(Strawberry.all_strawberries, Cherry.all_cherries, Banana.all_bananas)


        self.interact_elements = pygame.sprite.Group()
        self.interact_elements.add(FallingPlatform.all_falling_platforms)


        self.enemies = pygame.sprite.Group()
        BlueBird(34*block_size, HEIGHT - 5*block_size - 42, 32, 32, 120)
        BlueBird(33*block_size, HEIGHT - 7*block_size, 32, 32, 80)
        BlueBird(12*block_size, HEIGHT - 6*block_size, 32, 32, 240)
        Bunny(6*block_size, HEIGHT - 9*block_size + 12, 34, 44, 200, -1)
        Bunny(9*block_size, HEIGHT - 9*block_size + 12, 34, 44, 400, 1)
        Bunny(14*block_size, HEIGHT + block_size + 12, 34, 44, 200, 1)
        Bunny(8*block_size, HEIGHT + 3*block_size + 12, 34, 44, 200, 1)
        self.enemies.add(Bunny.all_bunnies, BlueBird.all_bluebirds)

    def clear_map(self):
        # Wyczyszczenie mapy
        self.objects = []
        self.objects_notcoll = []
        for sup in self.superiors:
            sup.kill()
        for elem in self.interact_elements:
            elem.kill()
        for enemy in self.enemies:
            enemy.kill()