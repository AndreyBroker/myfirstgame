from typing import Any
import pygame
from pygame.locals import *
from sys import exit

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
        self.pos_y_inicial = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]
        self.jumping = False
        self.wallking = False

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


        if self.wallking:

            self.current_sprite += 0.1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]

    def jump(self):
        self.jumping = True

    def wallk(self):
        self.wallking = True

    def stop(self):
        self.wallking = False


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

            self.current_sprite += 1


            print("right",self.current_sprite)

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]
        elif self.wallking_right:

            self.current_sprite -= 1

            if self.current_sprite < 0:

                print(len(self.sprites))
                self.current_sprite = 299

            self.image = self.sprites[int(self.current_sprite)]
     
    def move_left(self):
        # self.rect.x += steps
        self.wallking_left = True

    def move_right(self):
        # self.rect.x += steps
        self.wallking_right = True


    def stop(self):

        self.wallking_left = False
        self.wallking_right = False

        

## Defini o tamanho da tela
screen_width = 768
screen_height = 384

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Socioly Game')

background_image = Background(0, 0)
moving_sprites = pygame.sprite.Group()
player = Player(0, 230)

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

    if any(keys):
        player.wallk()
    else:
        player.stop()

    if keys[K_d]:
        background_image.move_left()

    elif keys[K_a]:
        background_image.move_right()
    
    if not keys[K_d] and not keys[K_a]:
        background_image.stop()


    moving_sprites.update()
    moving_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
