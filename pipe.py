import pygame as pg
from random import randint
from settings import *


class Pipe:
    def __init__(self):
        self.bot_img = pg.image.load("./images/bottom_pipe.png").convert_alpha()
        self.top_img = pg.image.load("./images/top_pipe.png").convert_alpha()
        self.height = self.top_img.get_height()
        self.width = self.top_img.get_width()
        self.spacing = 150
        self.y = 100 + 25 * randint(0, 6)
        self.x = WIDTH
        self.speed = 20
        self.goal = self.x + self.width
        self.top_rect = pg.Rect(self.x, self.y - self.height, self.width, self.height)
        self.bot_rect = pg.Rect(self.x, self.y + self.spacing, self.width, self.height)
        self.pipes = [self.bot_rect, self.top_rect]

    def update(self, bird, dt):
        if bird.alive:
            self.x -= self.speed * dt
            if self.x + self.width < 0:
                self.reset()
            self.goal = self.x + self.width / 2
            self.top_rect.x = self.x
            self.bot_rect.x = self.x

    def reset(self):
        self.y = 100 + 25 * randint(0, 6)
        self.top_rect.y = self.y - self.height
        self.bot_rect.y = self.y + self.spacing
        self.x = WIDTH

    def draw(self):
        SCREEN.blit(
            self.top_img, (self.x, self.y - self.height, self.width, self.height)
        )
        SCREEN.blit(
            self.bot_img, (self.x, self.y + self.spacing, self.width, self.height)
        )
