import pygame

def bot_handle_vertical_collsion(player, objects, interact_elements, enemies, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            collided_objects.append(obj)
    for obj in interact_elements:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            collided_objects.append(obj)
    for obj in enemies:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            collided_objects.append(obj)
    return collided_objects

def top_handle_vertical_collsion(player, objects, interact_elements, enemies, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()
            collided_objects.append(obj)
    for obj in interact_elements:
        if pygame.sprite.collide_mask(player, obj):
            if dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()
            collided_objects.append(obj)
    for obj in enemies:
        if pygame.sprite.collide_mask(player, obj):
            if dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()
                
            collided_objects.append(obj)
    return collided_objects

def collect_superiors(player, superiors):
    collided_objects = []
    for obj in superiors:
        if pygame.sprite.collide_mask(player, obj):
            collided_objects.append(obj)
    return collided_objects

def collide(player, objects, interact_elements, enemies, dx):
    player.move(dx, 0)
    player.update()
    collided_objects = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_objects=(obj)
            break
    for obj in interact_elements:
        if pygame.sprite.collide_mask(player, obj):
            collided_objects=(obj)
            break
    for obj in enemies:
        if pygame.sprite.collide_mask(player, obj):
            collided_objects=(obj)
            break
    player.move(-dx, 0)
    player.update()
    return collided_objects
        



