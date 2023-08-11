from typing import Any
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = {"right": [], "left": []}
        for i in range(1, 3):
            self.sprites["right"].append(pygame.transform.scale(pygame.image.load(f'./Images/Runing Animation/image ({i}).png'), (50, 64)))
        for i in range (3, 5):
            self.sprites["left"].append(pygame.transform.scale(pygame.image.load(f'./Images/Runing Animation/image ({i}).png'), (50, 64)))
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

        # print(f"Player: x: {self.rect.x}, {self.rect.y}")

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

class Missel(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = {"right": [], "left": []}
        for i in range(1, 8):
            self.sprites["right"].append(pygame.transform.scale(pygame.image.load(f'./Images/Missel Animation/right/Missel right ({i}).png'), (100, 30)))
        for i in range(1, 8):
            self.sprites["left"].append(pygame.transform.scale(pygame.image.load(f'./Images/Missel Animation/left/Missel left ({i}).png'), (100, 30)))
        self.current_sprite = 0
        self.image = self.sprites["left"][self.current_sprite]
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_y_inicial = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]
        self.iscommig = False
        self.animation = self.Animation(self)


    def update(self):

        # print(f"Missel: x: {self.rect.x}, {self.rect.y}")

        if self.iscommig:

            self.rect.x -= 6
            self.animation.basic()

            if self.rect.x <= - 110:
                self.rect.x = 770
                self.iscommig = False

    def shot(self):
        self.iscommig = True

    def colision(self):
        self.iscommig = False
        self.rect.x = 770


    class Animation:

        def __init__(self, parent):
            self.parent = parent

        def basic(self):

            self.parent.current_sprite += 0.3

            if self.parent.current_sprite >= len(self.parent.sprites["left"]):
                self.parent.current_sprite = 0

            self.parent.image = self.parent.sprites["left"][int(self.parent.current_sprite)]

