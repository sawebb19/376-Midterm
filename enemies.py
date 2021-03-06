import sys
sys.path.append("../CIS-376-Pygame-Engine/")

from Engine import *
from Scene import *
from game_objects import *
import pygame as pg

class Enemy(DUGameObject):
    def __init__(self, eng, x=0, y=0, lb=0, rb=1024):
        super().__init__()
        self.images = [[],[]] # [0][x] for facing left, [1][x] for facing right
        for i in range(1,11):
            self.images[1].append(pg.image.load("./zombie/Walk ("+str(i)+").png").convert_alpha())
            self.images[1][i-1] = self.images[1][i-1].subsurface(self.images[1][i-1].get_bounding_rect())
            self.images[1][i-1] = pg.transform.scale(self.images[1][i-1], (128, 128)) 
            self.images[0].append(pg.transform.flip(self.images[1][i-1], True, False))
        self.image = self.images[1][0]
        self.rect = self.image.get_rect()
        self.dirty = 2
        self.direction = 0 # 0 for left, 1 for right
        self.speed = 1
        self.x = x
        self.y = y
        self.walk_time = 0
        self.current_frame = 0
        self.eng = eng
        self.lb = lb
        self.rb = rb

    # Enemies simply walk back and forth, turning around at screen or platform edges
    def update(self):
        self.walk_time = self.walk_time + self.eng.deltaTime
        if self.walk_time > .1:
            self.current_frame = (self.current_frame + 1 ) % 10
            self.walk_time = 0
        self.image = self.images[self.direction][self.current_frame]

        if (self.x <= self.lb or self.x >= self.rb - 128):
            self.direction = abs(self.direction - 1)
        self.x = self.x + 100 * (self.direction - 0.5) * 2 * self.speed * self.eng.deltaTime
        
        self.rect.x = self.x
        self.rect.y = self.y