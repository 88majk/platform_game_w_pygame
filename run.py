import pygame

from graphic_setup import *
from collisions import *
from player import Player
from block import Block
from menu import *
from levels.level1 import *
from levels.level2 import *
from picture import Picture
from pygame.locals import *

FPS = 60
PLAYER_VEL = 5
level_win = [False]

def handle_move(player, objects, superiors): # FUNKCJA STEROWANIA
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
    
    # SPRAWDZANIE I OBSLUGA KOLIZJI POSTACI
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

    # LISTY POTRZEBNE DO RYSOWANIA ZESTAWOW PRZYCISKOW W ZALEZNOSCI OD STANU
    menu_buttons = [levels_button, settings_button, exit_button]
    levels_buttons = [level01_button, level02_button, level03_button, backFromLvls_button]
    pause_buttons = [restart_button, exit_from_game_button]
    win_buttons = [levels_endlvl_button, restart_endlvl_button]

    # LISTA DO RYSOWANIA TLA MENU GLOWNEGO
    menu_floor = [Block(i*block_size, HEIGHT - block_size, block_size, 96, 0) for i in range(-WIDTH // block_size, WIDTH * 2//block_size)]

    ##### STANY #####
    play_state = False # STAN GRY - WYSWIETLANIE MAPY ORAZ BOHATERA
    levels_choice = False # WYBOR LEVELU - WYSWIETLANIE CZESCI MENU Z WYBOREM POZIOMU
    menu_state = True # POCZATKOWY STAN WYSWIETLANIA MENU
    pause_state = False # STAN WYSTEPUJACY W TRAKCIE STANU PLAY STATE - PAUZA W GRZE
    run = True # OGOLNY STAN GLOWNEJ PETLI PROGRAMU

    while run:
        while menu_state:
            clock.tick(FPS) 
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass

            if mark_button(levels_button):
                menu_state = False
                levels_choice = True
            if mark_button(exit_button):
                menu_state = False
                run = False
            if mark_button(settings_button):
                pass
            
            draw_menu(window, background, bg_image, menu_floor, 0)
            draw_buttons(window, menu_buttons)
            draw_text(window, "PJF Adventures", title_font, TITLE_COL, 50, 50)
            draw_text(window, "Levels", font, TEXT_COL, 180, 255)
            draw_text(window, "Settings", font, TEXT_COL, 180, 315)
            draw_text(window, "Exit", font, TEXT_COL, 180, 370)

        while levels_choice:
            clock.tick(FPS)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pass
            
            if mark_button(level01_button):
                level = Level1()
                level_reset = True
                play_state = True
                levels_choice = False
            if mark_button(level02_button):
                level = Level2()
                level_reset = True
                play_state = True
                levels_choice = False
            if mark_button(backFromLvls_button):
                menu_state = True
                levels_choice = False

            draw_menu(window, background, bg_image, menu_floor, 0)
            draw_buttons(window, levels_buttons)
            draw_text(window, "PJF Adventures", title_font, TITLE_COL, 50, 50)
            draw_text(window, "Choose level", font, TEXT_COL, 120, 280)
            draw_text(window, "Back to menu", font, TEXT_COL, 150, 416)
        
        while play_state:
            clock.tick(FPS)
            pygame.display.update()

            if level_reset:
                offset_x = 0
                level.reset_level()
                player = Player(80, 100, 50, 50)
                player.score = 0
                player.life_points = 3
                level_reset = False

            # ODCZYT KLAWISZY
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        play_state = False
                        run = False
                        break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.jump_count < 2:
                        player.jump()
                    if event.key == pygame.K_ESCAPE:
                        play_state = False
                        pause_state = True

            #### PAUZA W GRZE #####################################################
            while pause_state:
                clock.tick(FPS)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            play_state = True
                            pause_state = False

                if mark_button(exit_from_game_button):
                    level_reset = True
                    level.clear_map()
                    pause_state = False
                    play_state = False
                    menu_state = True
                if mark_button(restart_button):
                    level_reset = True
                    level.clear_map()
                    pause_state = False
                    play_state = True


                frame = Picture(frame_img, 1)
                frame.draw(window, 265, 140)
                draw_text(window, "Paused", font, (66, 45, 32), 420, 200)
                draw_text(window, "Restart level", smaller_font,  (66, 45, 32), 450, 250)
                draw_text(window, "Exit to menu", smaller_font,  (66, 45, 32), 450, 280)
                draw_buttons(window, pause_buttons) # 400, 250
            ######################################################################
            

            # WARUNEK SKONCZENIA POZIOMU (ZEBRANIA FLAGI FINAL) ORAZ WYSWIETLENIE MENU
            while level_win[0]:
                clock.tick(FPS)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pass

                if mark_button(levels_endlvl_button):
                    level_reset = True
                    level.clear_map()
                    player.kill()
                    play_state = False
                    levels_choice = True
                    level_win[0] = False
                if mark_button(restart_endlvl_button):
                    level_reset = True
                    level.clear_map()
                    player.kill()
                    level_win[0] = False
                    play_state = True

                frame_win = Picture(frame_img, 1)
                frame_win.draw(window, 265, 140)
                draw_text(window, "You won!", font, (66, 45, 32), 420, 200)
                draw_text(window, "Switch level", smaller_font,  (66, 45, 32), 450, 250)
                draw_text(window, "Restart level", smaller_font,  (66, 45, 32), 450, 280)
                draw_buttons(window, win_buttons)
            ##########################################################
                
            
            # WARUNEK UTRATY WSZYSTKICH ZYC (GAME OVER)
            while player.life_points == 0:
                clock.tick(FPS)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pass

                if mark_button(levels_endlvl_button):
                    level_reset = True
                    level.clear_map()
                    player.kill()
                    play_state = False
                    levels_choice = True
                    break
                if mark_button(restart_endlvl_button):
                    level_reset = True
                    level.clear_map()
                    player.kill()
                    play_state = True
                    break

                frame_win = Picture(frame_img, 1)
                frame_win.draw(window, 265, 140)
                draw_text(window, "Game over", font, (66, 45, 32), 420, 200)
                draw_text(window, "Switch level", smaller_font,  (66, 45, 32), 450, 250)
                draw_text(window, "Restart level", smaller_font,  (66, 45, 32), 450, 280)
                draw_buttons(window, win_buttons)
            ##########################################################

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
            heart_img = pygame.image.load("assets/Other/heart.png").convert_alpha()
            hearts = [Picture(heart_img, 2) for i in range (1, player.life_points + 1)]
            for i, heart in enumerate(hearts):
                heart.draw(window, 950 - 55*i, 10)      

            # PRZEWIJANIE MAPY
            if((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
                offset_x += player.x_vel     

    print("wyszlo sie")       
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)