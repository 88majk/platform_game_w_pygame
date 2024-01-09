import pygame
from button import Button
from object import Object
from graphic_setup import load_sprite_sheets


font = pygame.font.SysFont("Retro Gaming", 30)
smaller_font = pygame.font.SysFont("Retro Gaming", 18)
title_font = pygame.font.SysFont("04b 30", 76)
heart = pygame.font.SysFont("Times New Roman", 30)
TEXT_COL = (255, 255, 255)
TITLE_COL = (16, 112, 37)

font_score = pygame.font.SysFont("04b 30", 45)
SCORE_COL = (158, 13, 20)

play_img = pygame.image.load("assets/Menu/Buttons/play.png").convert_alpha()
back_img = pygame.image.load("assets/Menu/Buttons/Back.png").convert_alpha()


#### PRZYCISKI MENU GLOWNEGO
levels_img = pygame.image.load("assets/Menu/Buttons/Levels.png").convert_alpha()
levels_button = Button(180, 250, levels_img, 2)

settings_img = pygame.image.load("assets/Menu/Buttons/settings.png").convert_alpha()
settings_button = Button(180, 310, settings_img, 2)

exit_img = pygame.image.load("assets/Menu/Buttons/close.png").convert_alpha()
exit_button = Button(180, 370, exit_img, 2.6)

instruction_pic = pygame.image.load("assets/Other/instruction.png")


#### PRZYCISKI MENU WYBORU LEVELU
level01_img = pygame.image.load("assets/Menu/Levels/01.png").convert_alpha()
level01_button = Button(130, 330, level01_img, 2)

level02_img = pygame.image.load("assets/Menu/Levels/02.png").convert_alpha()
level02_button = Button(180, 330, level02_img, 2)

level03_img = pygame.image.load("assets/Menu/Levels/03.png").convert_alpha()
level03_button = Button(230, 330, level03_img, 2)
backFromLvls_button = Button(120, 420, back_img, 2)


#### PRZYCISKI MENU USTAWIEN
ninjafrog_img = pygame.image.load("assets/Other/ninjafrog.png")
ninjafrog_button = Button(130, 330, ninjafrog_img, 2.5)

virtualguy_img = pygame.image.load("assets/Other/virtualguy.png")
virtualguy_button = Button(210, 330, virtualguy_img, 2.5)

pinkman_img = pygame.image.load("assets/Other/pinkman.png")
pinkman_button = Button(290, 330, pinkman_img, 2.5)

backFromSettings_button = Button(120, 470, back_img, 2)


#### PRZYCISKI MENU PAUZY GRY
frame_img = pygame.image.load("assets/Other/frame1.png").convert_alpha()
restart_img = pygame.image.load("assets/Menu/Buttons/Restart.png").convert_alpha()
restart_button = Button(550, 250, restart_img, 1.1)
exit_from_game_button = Button(550, 280, back_img, 1.5)



#### PRZYCISKI EKRANU KONCA POZIOMU
levels_endlvl_button = Button(550, 250, levels_img, 1)
restart_endlvl_button = Button(550, 280, restart_img, 1)