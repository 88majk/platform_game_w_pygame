import pygame
from button import Button
from object import Object

font = pygame.font.SysFont("Retro Gaming", 30)
title_font = pygame.font.SysFont("04b 30", 70)
heart = pygame.font.SysFont("Times New Roman", 30)
TEXT_COL = (255, 255, 255)
TITLE_COL = (16, 112, 37)

font_score = pygame.font.SysFont("04b 30", 45)
SCORE_COL = (158, 13, 20)

play_img = pygame.image.load("assets/Menu/Buttons/play.png").convert_alpha()
back_img = pygame.image.load("assets/Menu/Buttons/Back.png").convert_alpha()

level01_img = pygame.image.load("assets/Menu/Levels/01.png").convert_alpha()
level01_button = Button(130, 250, level01_img, 2)
level02_img = pygame.image.load("assets/Menu/Levels/02.png").convert_alpha()
level02_button = Button(160, 250, level02_img, 2)
level03_img = pygame.image.load("assets/Menu/Levels/03.png").convert_alpha()
level03_button = Button(190, 250, level03_img, 2)


levels_img = pygame.image.load("assets/Menu/Buttons/Levels.png").convert_alpha()
levels_button = Button(130, 250, levels_img, 2)

settings_img = pygame.image.load("assets/Menu/Buttons/settings.png").convert_alpha()
settings_button = Button(130, 310, settings_img, 2)

exit_img = pygame.image.load("assets/Menu/Buttons/close.png").convert_alpha()
exit_button = Button(130, 370, exit_img, 2.6)