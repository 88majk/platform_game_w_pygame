import pygame
from graphic_setup import *
from collisions import *
from object import Object
from player import Player
from ground.block import Block
from ground.falling_platform import FallingPlatform
from obstacles.fire import Fire
from obstacles.spikes import Spikes
from superiors.strawberry import Strawberry
from obstacles.final_flag import FinalFlag

class Level1():
    
    def reset_level(self):
        block_size = 96
        self.floor = [Block(i*block_size, HEIGHT - block_size, block_size, 96, 0) for i in range(-WIDTH // block_size, WIDTH * 2//block_size)]
        self.final_flag = FinalFlag(1000, HEIGHT - block_size - 2*64, 64, 64)

        [FallingPlatform(i*100, HEIGHT - block_size - 4*16, 32, 10) for i in range(1, 22)]


        self.fire = []

        self.blocks = [Block(block_size * 3, HEIGHT - block_size * 4, block_size, 96, 0), 
                       Block(0, HEIGHT - block_size * 2, block_size, 96, 0),
                       Block(0, HEIGHT - block_size * 3, block_size, 96, 0),
                       Block(block_size * 5, HEIGHT - block_size * 6, block_size, 96, 0),
                       Block(block_size * 8, HEIGHT - block_size * 6, block_size, 96, 0)]
        
        self.spikes = [Spikes(i*100, HEIGHT - block_size - 2*16, 16, 16) for i in range(1, 22)]

        [Strawberry(i*50, HEIGHT - 5*block_size, 32, 32) for i in range (1,11)]
          

        self.objects = [*self.floor, *self.blocks, *self.fire, *self.spikes, self.final_flag]
        
        self.superiors = Strawberry.all_strawberries
        
        self.interact_elements = FallingPlatform.all_falling_platforms
    
    def clear_map(self):
        self.objects = []
        self.superiors.empty()
