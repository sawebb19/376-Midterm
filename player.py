import sys
sys.path.append("../CIS-376-Pygame-Engine")

from Engine import *
from Scene import *
from game_objects import *
import pygame as pg

class Player(DUGameObject):
    def __init__(self, eng, x=0, y=0):
        super().__init__()

        # TODO: Have different sprites for player
        self.images = [[],[]] # [0][x] for facing left, [1][x] for facing right
        for i in range(1,11):
            self.images[1].append(pg.image.load("./zombie/Walk ("+str(i)+").png").convert_alpha())
            self.images[1][i-1] = self.images[1][i-1].subsurface(self.images[1][i-1].get_bounding_rect())
            self.images[1][i-1] = pg.transform.scale(self.images[1][i-1], (128, 128)) 
            self.images[0].append(pg.transform.flip(self.images[1][i-1], True, False))
        self.image = self.images[1][0]
        self.rect = self.image.get_rect()
        self.dirty = 2
        self.direction = 1
        self.speed = 0
        self.x = x
        self.y = y
        self.walk_time = 0
        self.current_frame = 0
        self.eng = eng
        self.height = 15

    # TODO
    def update(self):
        self.walk_time = self.walk_time + self.eng.deltaTime
        if self.walk_time > .1:
            self.current_frame = (self.current_frame + 1 ) % 10
            self.walk_time = 0
        self.image = self.images[self.direction][self.current_frame]

        self.x = self.x + 100 * (self.direction - 0.5) * -2 * self.speed * self.eng.deltaTime

        if self.height != 15:
            self.y += (40 * self.height + ((self.height ** 3) / 3)) * self.eng.deltaTime
            self.height += 1

        self.rect.x = self.x
        self.rect.y = self.y

        for event in self.eng.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.direction = 0
                    self.speed = -2
                if event.key == pg.K_d:
                    self.direction = 1
                    self.image = pg.transform.flip(self.image, True, False)
                    self.speed = -2
                if (event.key == pg.K_SPACE and self.height == 15):
                    self.height = (self.height - 1) * -1
        
        pg.draw.rect(self.image, (0, 0, 255), self.image.get_bounding_rect(), width=1)
        pg.draw.rect(self.image, (255, 0, 0), self.image.get_rect(), width=1)

# TODO - having a camera tied to the player should be easier to manage
class Camera(UGameObject):
    pass

class Score(UGameObject):
    def __init__(self, eng):
        super().__init__()
        self.score = 0
        self.eng = eng

    def update(self):
        self.score = self.score + self.eng.deltaTime
        # Win condition
        if self.score >= 10000:
            self.eng.end()
        print(self.score)

    def getScore(self):
        return self.score