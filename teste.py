from typing import Any
import pygame
from pygame.locals import *
from sys import exit

from pygame.sprite import AbstractGroup

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('./Images/Runing Animation/image1.png'), (200, 200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./Images/Runing Animation/image2.png'), (200, 200)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]


    def update(self):
        self.current_sprite += 0.1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

    def jump(self, max_y):

        for alt in range(max_y):
            self.rect.topleft = [self.pos_x, self.pos_y - alt]
        

## Defini o tamanho da tela
screen_width = 650
screen_height = 406

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Socioly Game')

user_height = 200
user_width = 200

user_position_x = {"inicial": screen_width / 5, "flex": screen_width / 4}
user_position_y = {"inicial": 270, "flex": 270}

background_image = pygame.image.load('./Images/BackgroundImage.jpg')
moving_sprites = pygame.sprite.Group()
player = Player(0, user_position_y["flex"])
moving_sprites.add(player)

move_vel_x = 0
move_vel_y = 0
jumping = False

gravity = 0.2

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump(60)

    keys = pygame.key.get_pressed()

    if keys[K_d]:
        move_vel_x -= 2
    elif keys[K_a]:
        move_vel_x += 2
    
    moving_sprites.update()
    screen.blit(background_image, (move_vel_x, 0)) 
    screen.blit(background_image, (move_vel_x + background_image.get_width(), 0)) 

    moving_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
