import pygame

from graphic_setup import *
from collisions import *
from player import Player
from ground.block import Block
from menu import *
from levels.level1 import *
from levels.level2 import *
from picture import Picture
from pygame.locals import *

FPS = 50
PLAYER_VEL = 6
level_win = [False]

def handle_move(player, objects, interact_elements, superiors, enemies): # FUNKCJA STEROWANIA
    keys = pygame.key.get_pressed()
    player.x_vel = 0
    
    bot_vertical_collide = bot_handle_vertical_collsion(player, objects, interact_elements, enemies, 2*player.y_vel)
    top_vertical_collide = top_handle_vertical_collsion(player, objects, interact_elements, enemies, 2*player.y_vel)
    
    collide_left = collide(player, objects, interact_elements, enemies, -PLAYER_VEL * 2)
    collide_right = collide(player, objects, interact_elements, enemies, PLAYER_VEL * 2)

   
    if keys[pygame.K_a]:
        player.direction = "left"
        if not collide_left:
            player.move_left(PLAYER_VEL)
        else:
            player.slide(player.y_vel)
    if keys[pygame.K_d]:
        player.direction = "right"
        if not collide_right:
            player.move_right(PLAYER_VEL)
        else:
            player.slide(player.y_vel)

    superiors_collected = collect_superiors(player, superiors)
    
    # SPRAWDZANIE I OBSLUGA KOLIZJI POSTACI
    to_check = [collide_left, collide_right, *top_vertical_collide, *superiors_collected]
    enemies_hitlist = [collide_left, collide_right, *top_vertical_collide]

    for obj in bot_vertical_collide:
        if obj and obj.name == "fat_bird":
            obj.active = False
            obj.jumpedOn = True
        if obj and obj.name == "blue_bird":
            obj.active = False
            obj.jumpedOn = True
        if obj and obj.name == "bunny":
            obj.active = False
            obj.jumpedOn = True
    
    for obj in enemies_hitlist:
        if obj and obj.name == "fat_bird" and obj.active:
            player.make_hit()
        if obj and obj.name == "blue_bird" and obj.active:
            player.make_hit()
        if obj and obj.name == "bunny" and obj.active:
            player.make_hit()

    for obj in to_check + bot_vertical_collide:
        if obj and obj.name == "fire":
            player.make_hit()
        if obj and obj.name == "spikes":
            player.make_hit()
        if obj and obj.name == "saw":
            player.make_hit()
        if obj and obj.name == "spike_head":
            player.make_hit()
        if obj and obj.name == "spikedball":
            player.make_hit()
        if obj and obj.name == "chain":
            player.make_hit()

        if obj and obj.name == "falling_platforms":
            obj.jumpedOn = True

        if obj and obj.name == "strawberry" and not obj.collected:
            player.collect_points(10)
            if obj in superiors:
                obj.collected = True
        if obj and obj.name == "apple" and not obj.collected:
            player.collect_apple()
            if obj in superiors:
                obj.collected = True
        if obj and obj.name == "cherry" and not obj.collected:
            player.collect_points(10)
            if obj in superiors:
                obj.collected = True
        if obj and obj.name == "banana" and not obj.collected:
            player.collect_points(10)
            if obj in superiors:
                obj.collected = True
        if obj and obj.name == "pineapple" and not obj.collected:
            player.start_gravity_reduction()
            if obj in superiors:
                obj.collected = True

        if obj and obj.name == "final_flag":
            obj.collected = True
            
     


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Brown.png")
    block_size = 96
    
    offset_x = 0
    offset_y = 0
    scroll_area_width_x = 270
    scroll_area_width_y = 50

    picked_hero = "NinjaFrog"
    heart_img = pygame.image.load("assets/Other/heart.png").convert_alpha()

    # LISTY POTRZEBNE DO RYSOWANIA ZESTAWOW PRZYCISKOW W ZALEZNOSCI OD STANU
    menu_buttons = [levels_button, settings_button, exit_button]
    settings_buttons = [ninjafrog_button, virtualguy_button, pinkman_button, backFromSettings_button]
    rect_position = (130, 330)
    rect_size = (90, 90)
    levels_buttons = [level01_button, level02_button, level03_button, backFromLvls_button]
    pause_buttons = [restart_button, exit_from_game_button]
    win_buttons = [levels_endlvl_button, restart_endlvl_button]

    # LISTA DO RYSOWANIA TLA MENU GLOWNEGO
    menu_floor = [Block(i*block_size, HEIGHT - block_size, block_size, block_size, 96, 0) for i in range(-WIDTH // block_size, WIDTH * 2//block_size)]

    pygame.mouse.set_cursor(pygame.cursors.diamond) 

    ##### STANY #####
    play_state = False # STAN GRY - WYSWIETLANIE MAPY ORAZ BOHATERA
    settings_state = False # STAN USTAWIEN
    levels_choice = False # WYBOR LEVELU - WYSWIETLANIE CZESCI MENU Z WYBOREM POZIOMU
    menu_state = True # POCZATKOWY STAN WYSWIETLANIA MENU
    pause_state = False # STAN WYSTEPUJACY W TRAKCIE STANU PLAY STATE - PAUZA W GRZE
    run = True # OGOLNY STAN GLOWNEJ PETLI PROGRAMU

    while run:
        
        while menu_state:
            clock.tick(FPS) 
            pygame.display.update()
            background = update_background(background, 1)
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
                menu_state = False
                settings_state = True

            
            draw_menu(window, background, bg_image, menu_floor, 0, 0)
            draw_buttons(window, menu_buttons)
            draw_text(window, "PJF Adventures", title_font, TITLE_COL, 70, 50)
            draw_text(window, "Levels", font, TEXT_COL, 230, 255)
            draw_text(window, "Settings", font, TEXT_COL, 230, 315)
            draw_text(window, "Exit", font, TEXT_COL, 230, 370)
            instruction = Picture(instruction_pic, 2)
            instruction.draw(window, 590, 150)

        while levels_choice:
            clock.tick(FPS)
            pygame.display.update()
            background = update_background(background, 1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pass
            
            if mark_button(level01_button):
                SCORE_COL = (18, 130, 28)
                level = Level1()
                level_reset = True
                play_state = True
                levels_choice = False
            if mark_button(level02_button):
                SCORE_COL = (204, 33, 161)
                level = Level2()
                level_reset = True
                play_state = True
                levels_choice = False
            if mark_button(backFromLvls_button):
                menu_state = True
                levels_choice = False

            draw_menu(window, background, bg_image, menu_floor, 0, 0)
            draw_buttons(window, levels_buttons)
            draw_text(window, "PJF Adventures", title_font, TITLE_COL, 70, 50)
            draw_text(window, "Choose level", font, TEXT_COL, 120, 280)
            draw_text(window, "Back to menu", font, TEXT_COL, 150, 416)
        
        while settings_state:
            clock.tick(FPS)
            pygame.display.update()
            background = update_background(background, 1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        settings_state = False
                        menu_state = True

            if mark_button(ninjafrog_button):
                picked_hero = "NinjaFrog"
                rect_position = (130, 330)
            if mark_button(virtualguy_button):
                picked_hero = "VirtualGuy"
                rect_position = (210, 330)
            if mark_button(pinkman_button):
                picked_hero = "PinkMan"
                rect_position = (290, 330)
            if mark_button(backFromSettings_button):
                settings_state = False
                menu_state = True
            
            draw_menu(window, background, bg_image, menu_floor, 0, 0)
            draw_buttons(window, settings_buttons)
            draw_text(window, "PJF Adventures", title_font, TITLE_COL, 70, 50)
            draw_text(window, f"Pick your hero", font, (255,255,255), 120, 270)
            draw_text(window, "Back to menu", smaller_font, (255,255,255), 155, 475)
            pygame.draw.rect(window, (55, 163, 23), (*rect_position, *rect_size), 2)
            

        while play_state:
            clock.tick(FPS)
            pygame.display.update()
            background = update_background(background, 1)

            if level_reset:
                offset_x = 0
                offset_y = 0
                level.reset_level()
                player = Player(100, 100, 50, 50, picked_hero)
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
                background = update_background(background, 1)
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
                frame.draw(window, 415, 140)
                draw_text(window, "Paused", font, (66, 45, 32), 570, 200)
                draw_text(window, "Restart level", smaller_font,  (66, 45, 32), 580, 250)
                draw_text(window, "Exit to menu", smaller_font,  (66, 45, 32), 580, 280)
                draw_buttons(window, pause_buttons)
            ######################################################################
            
            # WARUNEK SKONCZENIA POZIOMU (ZEBRANIA FLAGI FINAL) ORAZ WYSWIETLENIE MENU
            while level_win[0]:
                clock.tick(FPS)
                pygame.display.update()
                background = update_background(background, 1)
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
                frame_win.draw(window, 415, 140)
                ### tutaj dodac gwiazdki za poziom
                draw_text(window, "You won!", font, (66, 45, 32), 570, 180)
                draw_text(window, f"Your score: {player.score}", smaller_font, (66, 45, 32), 557, 218)
                draw_text(window, "Switch level", smaller_font,  (66, 45, 32), 580, 250)
                draw_text(window, "Restart level", smaller_font,  (66, 45, 32), 580, 280)
                draw_buttons(window, win_buttons)
            ##########################################################
                
            
            # WARUNEK UTRATY WSZYSTKICH ZYC (GAME OVER)
            while player.life_points == 0 or player.rect.y > 3000:
                clock.tick(FPS)
                pygame.display.update()
                background = update_background(background, 1)
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
                frame_win.draw(window, 415, 140)
                draw_text(window, "Game over", font, (66, 45, 32), 570, 200)
                draw_text(window, "Switch level", smaller_font,  (66, 45, 32), 580, 250)
                draw_text(window, "Restart level", smaller_font,  (66, 45, 32), 580, 280)
                draw_buttons(window, win_buttons)
            ##########################################################

            # WŁĄCZANIE ANIMACJI
            player.loop(FPS)
            for obj in level.objects + level.objects_notcoll:
                obj.loop()
                if obj and obj.name == "final_flag": ##sprawdz warunek zebrania flagi (tutaj, zeby było płynne zakończenie poziomu)
                    if obj.lvl_end:
                        level_win[0] = True
                        player.win()
            for sup in level.superiors:
                sup.loop()
            for platform in level.interact_elements: 
                platform.loop()
            for sup in level.enemies:
                sup.loop()

            # RYSOWANIE ELEMENTOW MAPY
            handle_move(player, level.objects, level.interact_elements, level.superiors, level.enemies)
            draw(window, background, bg_image, player, level.objects, level.superiors, level.interact_elements, level.objects_notcoll, level.enemies, offset_x, offset_y)
            draw_text(window, str(player.score), font_score, SCORE_COL, 10, 10)
            
            # RYSOWANIE AKTUALNEJ LICZBY 
            hearts = [Picture(heart_img, 2) for i in range (1, player.life_points + 1)]
            for i, heart in enumerate(hearts):
                heart.draw(window, 1240 - 55*i, 10)      

            # PRZEWIJANIE MAPY PO X
            if((player.rect.right - offset_x >= WIDTH - scroll_area_width_x) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width_x) and player.x_vel < 0):
                offset_x += player.x_vel
            # PRZEIWJANIE MAPY PO Y
            if((player.rect.bottom - offset_y >= HEIGHT - scroll_area_width_y - 150) and player.y_vel > 0) or (
                (player.rect.top - offset_y <= scroll_area_width_y) and player.y_vel < 0):
                offset_y += player.y_vel     
     
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)