from typing import Any
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = {"right": [], "left": []}
        for i in range(1, 3):
            self.sprites["right"].append(pygame.transform.scale(pygame.image.load(f'./Images/Runing Animation/image ({i}).png'), (200, 200)))
        for i in range (3, 5):
            self.sprites["left"].append(pygame.transform.scale(pygame.image.load(f'./Images/Runing Animation/image ({i}).png'), (200, 200)))
        self.current_sprite = 0
        self.image = self.sprites["right"][self.current_sprite]
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_y_inicial = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]
        self.jumping = False
        self.walking_right = False
        self.walking_left = False
        # self.walking_left_animation = False
        # self.walking_right_animation = False
        self.animation = self.Animation(self)

    def update(self):

        if self.jumping:
            if self.rect.y < 130:
                self.jumping = False
            self.rect.y -= 5
        else:
            if self.rect.y < self.pos_y_inicial:

                self.rect.y += 5
            else:
                self.rect.y = self.pos_y_inicial

        if self.walking_left:
            self.rect.x -= 5
            self.animation.walking_left()
        
        if self.walking_right:
            self.rect.x += 5
            self.animation.walking_right()


    def jump(self):
        self.jumping = True

    def walk_right(self):
        self.stop_walk_lef()
        self.walking_right = True

    def walk_left(self):
        self.stop_walk_right()
        self.walking_left = True

    def stop_walk_right(self):
        self.walking_right = False

    def stop_walk_lef(self):
        self.walking_left = False


    class Animation():

        def __init__(self, parent):
            self.parent = parent

        def walking_right(self):

            self.parent.current_sprite += 0.2

            if self.parent.current_sprite > len(self.parent.sprites["right"]):
                self.parent.current_sprite = 0

            self.parent.image = self.parent.sprites["right"][int(self.parent.current_sprite)]

        def walking_left(self):

            self.parent.current_sprite += 0.2

            if self.parent.current_sprite > len(self.parent.sprites["left"]):
                self.parent.current_sprite = 0

            self.parent.image = self.parent.sprites["left"][int(self.parent.current_sprite)]


class Background(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []

        for i in range(1, 301):
            self.sprites.append(pygame.transform.scale(pygame.image.load(f'./Images/Background Animation/background ({i}).jpg'), (768, 384)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_y_inicial = pos_y
        self.pos_x_inicial = pos_x
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]
        self.wallking_left = False
        self.wallking_right = False


    def update(self):
        
        if self.wallking_left:

            self.current_sprite -= 1

            if self.current_sprite < 0:
                self.current_sprite = 299

            self.image = self.sprites[int(self.current_sprite)]

        elif self.wallking_right:

            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]
     
    def move_left(self):
        self.wallking_right = False
        self.wallking_left = True

    def move_right(self):
        self.wallking_left = False
        self.wallking_right = True


    def stop_move_right(self):
        self.wallking_right = False
    
    def stop_move_left(self):
        self.wallking_left = False


## Defini o tamanho da tela
screen_width = 768
screen_height = 384

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Socioly Game')

background_image = Background(0, 0)
moving_sprites = pygame.sprite.Group()
player = Player(50, 230)

moving_sprites.add(background_image)
moving_sprites.add(player)

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                player.jump()
        
    keys = pygame.key.get_pressed()


    # print(player.rect.x >= (screen_width - 250) or player.rect.x <= 40)

    if keys[K_d]:
        if(player.rect.x >= (screen_width - 250)):
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
            player.stop_walk_lef()
            player.animation.walking_left()
            background_image.move_left()
        else:
            player.walk_left()
    else:
        background_image.stop_move_left()
        player.stop_walk_lef()
        
    
    moving_sprites.update()
    moving_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
