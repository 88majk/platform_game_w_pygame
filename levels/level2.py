import pygame
from graphic_setup import *
from collisions import *
from object import Object
from player import Player
from ground.block import Block
from obstacles.fire import Fire
from obstacles.spikes import Spikes
from superiors.strawberry import Strawberry
from obstacles.final_flag import FinalFlag

class Level2():
    
    def reset_level(self):
        block_size = 96
        self.floor = [Block(i*block_size, HEIGHT - block_size, block_size, 96, 128) for i in range(-WIDTH // block_size, WIDTH * 2//block_size)]
        
        self.fire = [Fire(200, HEIGHT - block_size - 64, 16, 32)]
        self.final_flag = FinalFlag(1000, HEIGHT - block_size - 2*64, 64, 64)
        self.spikes = [Spikes(i*50, HEIGHT - block_size - 2*16, 16, 16) for i in range(2, 22)]

        [Strawberry(i*50, HEIGHT - 5*block_size, 32, 32) for i in range (1,11)]
        [Strawberry(i*50, HEIGHT - 2*block_size, 32, 32) for i in range (11,21)]

        self.superiors = Strawberry.all_strawberries  
        
        self.objects = [*self.floor, Block(0, HEIGHT - block_size * 2, block_size, 96, 128), 
                        Block(block_size * 3, HEIGHT - block_size * 4, block_size, 96, 128),
                        Block(block_size * 3, HEIGHT - block_size * 6, block_size, 96, 128),
                        self.final_flag, *self.spikes]
        
        self.interact_elements = []
    
    def clear_map(self):
        self.objects = []
        self.superiors.empty()
