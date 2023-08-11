from typing import Any
import pygame
from pygame.locals import *
from sys import exit
from objetos import Background, Player, Missel
import time
import random

pygame.init()

## Defini o tamanho da tela
screen_width = 768
screen_height = 384

preto = (0, 0, 0)
branco = (255, 255, 255)
verde = (0, 255, 0)

lifes = 3
ponts = 0
font = pygame.font.SysFont('04b_03', 20, False, False)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Socioly Game')

background_image = Background(0, 0)
player = Player(50, 290)
missel = Missel(770, 300)

moving_sprites = pygame.sprite.Group()
moving_sprites.add(background_image)
moving_sprites.add(player)
moving_sprites.add(missel)

clock = pygame.time.Clock()

last_time = time.time()
time_out = 5

while True:

    screen.fill((0, 0, 0))
    lifes_label = font.render(f"<3 {lifes}", False, (255, 0, 0))
    ponts_labal = font.render(f"{ponts}", False, (255, 255, 255))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                player.jump()

            if event.key == pygame.K_h:
                missel.shot()
        
    keys = pygame.key.get_pressed()


    if (time.time() - last_time) > time_out:
        missel.shot()
        last_time = time.time()
        time_out = random.randint(4, 8)

    if keys[K_d]:
        if(player.rect.x >= (screen_width - 250)):

            ponts+=1
            player.stop_walk_right()
            player.animation.walking_right()
            background_image.move_right()
        else:
            player.walk_right()
    else:
        background_image.stop_move_right()
        player.stop_walk_right()
    
    if keys[K_a]:
        if(player.rect.x <= 40):
            ponts-=1
            player.stop_walk_lef()
            player.animation.walking_left()
            background_image.move_left()
        else:
            player.walk_left()
    else:
        background_image.stop_move_left()
        player.stop_walk_lef()

    if (missel.rect.x >= player.rect.x and missel.rect.x <= player.rect.x + 50) and (missel.rect.y >= player.rect.y and missel.rect.y <= player.rect.y + 64):
        missel.colision()
        if(lifes - 1) < 0:
            ponts -= 1500
            lifes = 3
        else:
            lifes-=1
            ponts -= 500
            
    moving_sprites.update()
    moving_sprites.draw(screen)

    screen.blit(lifes_label, (650, 40))
    screen.blit(ponts_labal, (200, 40))
    pygame.display.flip()
    clock.tick(60)
