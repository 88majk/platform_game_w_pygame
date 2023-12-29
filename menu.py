import pygame
from button import Button
from object import Object

font = pygame.font.SysFont("Consolas", 40)
title_font = pygame.font.SysFont("04b 30", 70)
TEXT_COL = (255, 255, 255)
TITLE_COL = (16, 112, 37)

font = pygame.font.SysFont("Consolas", 30)
TEXT_COL = (255, 255, 255)

play_img = pygame.image.load("assets/Menu/Buttons/play.png").convert_alpha()
play_button = Button(130, 250, play_img, 1)

settings_img = pygame.image.load("assets/Menu/Buttons/settings.png").convert_alpha()
settings_button = Button(130, 290, settings_img, 1)

exit_img = pygame.image.load("assets/Menu/Buttons/close.png").convert_alpha()
exit_button = Button(130, 330, exit_img, 1)