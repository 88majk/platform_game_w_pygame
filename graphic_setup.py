import os, random, math
import pygame
from os import listdir
from os.path import isfile, join

WIDTH, HEIGHT = 1000, 780
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_text(window, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x,y))


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction = False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites
    return all_sprites



def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    return tiles, image


def mark_button(button):
    action = False

    pos = pygame.mouse.get_pos()

    if button.rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1 and button.clicked == False:
            button.clicked = True
            action = True
    
    if pygame.mouse.get_pressed()[0] == 0:
        button.clicked = False
    return action  


def draw(window, background, bg_image, player, objects, superiors, offset_x):
    for tile in background:
        window.blit(bg_image, tile)

    for object in objects:
        object.draw(window, offset_x)
    
    for sup in superiors:
        sup.draw(window, offset_x)

    player.draw(window, offset_x)


def draw_menu(window, background, bg_image, objects, offset_x):
    for tile in background:
        window.blit(bg_image, tile)  

    for object in objects:
        object.draw(window,offset_x)

def draw_buttons(window, buttons):
    for button in buttons:
        button.draw(window, 0)
        