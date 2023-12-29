import os, random, math
import pygame
from os import listdir
from os.path import isfile, join
from pygame.sprite import Group

from graphic_setup import *
from collisions import *
from object import Object
from player import Player
from block import Block
from fire import Fire
from strawberry import Strawberry
from button import Button
from menu import *

FPS = 60
PLAYER_VEL = 5

def handle_move(player, objects, superiors): # funkcja sterująca klawiszami
    keys = pygame.key.get_pressed()
    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2)
    collide_right = collide(player, objects, PLAYER_VEL * 2)

    if keys[pygame.K_a] and not collide_left:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_d] and not collide_right:
        player.move_right(PLAYER_VEL)

    vertical_collide = handle_vertical_collsion(player, objects, player.y_vel)
    superiors_collected = collect_superiors(player, superiors)

    to_check = [*collide_left, *collide_right, *vertical_collide, *superiors_collected]
    for obj in to_check:
        if obj and obj.name == "fire":
            player.make_hit()
        if obj and obj.name == "Strawberry":
            player.collect_straw()
            obj.collected()
            if obj in superiors:
                pass
                # superiors.remove(obj)
           


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Purple.png")

    block_size = 96

    floor = [Block(i*block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, WIDTH * 2//block_size)]
    
    fire = Fire(100, HEIGHT - block_size - 64, 16, 32)
    fire.on()

    strawberry = Strawberry(200, HEIGHT - 3*block_size, 32, 32)
    superiors = [Strawberry(i*block_size, HEIGHT - 3*block_size, 32, 32) for i in range (1, 12)]
    
    player = Player(100, 100, 50, 50)
    objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size), Block(block_size * 3, HEIGHT - block_size * 4, block_size), fire]
    
    offset_x = 0
    scroll_area_width = 200

    menu_buttons = [play_button, settings_button, exit_button]

    play_state = False
    menu_state = True
    run = True
    while run:
        while menu_state:
            clock.tick(FPS)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.jump_count < 2:
                        player.jump()
                    if event.key == pygame.K_ESCAPE:
                        play_state = False

            
            if mark_button(exit_button):
                menu_state = False
                run = False
            if mark_button(play_button):
                play_state = True
                menu_state = False
            if mark_button(settings_button):
                pass
            
            draw_menu(window, background, bg_image, floor, 0, menu_buttons)
            draw_text(window, "PJF Adventures", title_font, TITLE_COL, 50, 50)
            draw_text(window, "Play", font, TEXT_COL, 150, 250)
            draw_text(window, "Settings", font, TEXT_COL, 150, 290)
            draw_text(window, "Exit", font, TEXT_COL, 150, 330)

        while play_state:
            clock.tick(FPS)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.jump_count < 2:
                        player.jump()
                    if event.key == pygame.K_ESCAPE:
                        play_state = False
                        menu_state = True

            player.loop(FPS)
            fire.loop()
            for strawberry in superiors:
                strawberry.loop()

            handle_move(player, objects, superiors)
            draw(window, background, bg_image, player, objects, superiors, offset_x)
            draw_text(window, str(player.score), font_score, SCORE_COL, 10, 10)

            if((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
                offset_x += player.x_vel
                objects
            
            # if player.life_points == 0:
            #     play_state = False
            #     menu_state = True
        
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)