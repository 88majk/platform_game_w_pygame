import os, random, math
import pygame
from os import listdir
from os.path import isfile, join
from pygame.sprite import Group

from graphic_setup import *
from collisions import *
from player import Player
from block import Block
from menu import *
from levels.level1 import *
from picture import Picture

FPS = 60
PLAYER_VEL = 5
level_win = [False]

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
        if obj and obj.name == "spikes":
            player.make_hit()
        if obj and obj.name == "Strawberry" and not obj.collected:
            player.collect_straw()
            if obj in superiors:
                obj.collected = True
        if obj and obj.name == "final_flag":
            level_win[0] = True
            player.win()
           


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Purple.png")
    block_size = 96
    
    offset_x = 0
    scroll_area_width = 200

    menu_buttons = [levels_button, settings_button, exit_button]
    levels_buttons = [level01_button, level02_button, level03_button]
    menu_floor = [Block(i*block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, WIDTH * 2//block_size)]

    play_state = False
    menu_state = True
    level_reset = True
    run = True
    while run:
        if level_reset:
            level = Level1()
            level.reset_level()
            level_reset = False
            player = Player(100, 100, 50, 50)
            player.score = 0
            player.life_points = 3

        while menu_state:
            clock.tick(FPS)
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        play_state = False

            if mark_button(levels_button):
                levels_choice = True
                menu_state = False
            if mark_button(exit_button):
                menu_state = False
                run = False
            # if mark_button(play_button):
            #     play_state = True
            #     menu_state = False
            if mark_button(settings_button):
                pass
            
            
            draw_menu(window, background, bg_image, menu_floor, 0, menu_buttons)
            draw_text(window, "PJF Adventures", title_font, TITLE_COL, 50, 50)
            draw_text(window, "Levels", font, TEXT_COL, 180, 255)
            draw_text(window, "Settings", font, TEXT_COL, 180, 315)
            draw_text(window, "Exit", font, TEXT_COL, 180, 370)

        while levels_choice:
            clock.tick(FPS)
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu_state = True
                        levels_choice = False

            draw_menu(window, background, bg_image, menu_floor, 0, levels_button)
            draw_text(window, "PJF Adventures", title_font, TITLE_COL, 50, 50)
            draw_text(window, "Choose level", font, TEXT_COL, 180, 300)
            

        while play_state:
            clock.tick(FPS)
            pygame.display.update()

            # ODCZYT KLAWISZY
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.jump_count < 2:
                        player.jump()
                    if event.key == pygame.K_ESCAPE:
                        play_state = False
                        menu_state = True

            # WŁĄCZANIE ANIMACJI
            player.loop(FPS)
            for fire in level.fire:
                fire.loop()
            for strawberry in level.superiors:
                strawberry.loop()
            level.final_flag.loop()

            # RYSOWANIE ELEMENTOW MAPY
            handle_move(player, level.objects, level.superiors)
            draw(window, background, bg_image, player, level.objects, level.superiors, offset_x)
            draw_text(window, str(player.score), font_score, SCORE_COL, 10, 10)
            
            # RYSOWANIE AKTUALNEJ LICZBY ZYC
            heart_img = pygame.image.load("assets/Menu/Buttons/play.png").convert_alpha()
            hearts = [Picture(heart_img, 2) for i in range (1, player.life_points + 1)]
            for i, heart in enumerate(hearts):
                heart.draw(window, 950 - 50*i, 10)      

            # PRZEWIJANIE MAPY
            if((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
                offset_x += player.x_vel
                
            # CZYSZCZENIE MAPY PO UTRACIE ŻYĆ
            if player.life_points == 0:
                offset_x = 0
                level.clear_map()
                player.kill()
                play_state = False
                menu_state = True
                level_reset = True
            
            # WARUNEK SKONCZENIA POZIOMU (ZEBRANIA FLAGI FINAL )
            if level_win[0]:
                offset_x = 0
                level_win[0] = False
                level.clear_map()
                player.kill()
                play_state = False
                menu_state = True
                level_reset = True    

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)