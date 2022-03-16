import sys
from tkinter import font

from enemies import Enemy
sys.path.append("../CIS-376-Pygame-Engine")

from Engine import *
from Scene import *
from game_objects import *
import pygame as pg
import time

class Player(DUGameObject):
    def __init__(self, eng, x=0, y=0):
        super().__init__()
        self.size = 64
        self.images = [[],[]] # [0][x] for facing left, [1][x] for facing right
        for i in range(1,11):
            self.images[1].append(pg.image.load("./player/Walk ("+str(i)+").png").convert_alpha())
            self.images[1][i-1] = self.images[1][i-1].subsurface(self.images[1][i-1].get_bounding_rect())
            self.images[1][i-1] = pg.transform.scale(self.images[1][i-1], (self.size, self.size)) 
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
        self.fallcheck = False
        self.failscreen = pg.Surface((1000,1000))

    def update(self):
        self.walk_time = self.walk_time + self.eng.deltaTime
        if self.walk_time > .1:
            self.current_frame = (self.current_frame + 1 ) % 10
            self.walk_time = 0
        self.image = self.images[self.direction][self.current_frame]

        self.x = self.x + 100 * (self.direction - 0.5) * -2 * self.speed * self.eng.deltaTime

        if self.height != 15 or self.fallcheck:
            velocity = (40 * self.height + ((self.height ** 3) / 3)) * .03
            self.y += velocity
            if velocity >= 0:
                if abs(self.rect.y - 355 - 64) < 10:
                    if (self.rect.x > 600 - (self.size / 2) and self.rect.x < 950 - (self.size / 2)) or (self.rect.x > 74 - (self.size / 2) and self.rect.x < 424 - (self.size / 2)):
                        self.height = 14
                        self.y = 355 + 64
                        self.fallcheck = True
                    else:
                        self.height = 5
                if abs(self.rect.y - 195 - 64) < 10:
                    if (self.rect.x > 360 - (self.size / 2) and self.rect.x < 660 - (self.size / 2)):
                        self.height = 14
                        self.y = 195 + 64
                        self.fallcheck = True
                    else:
                        self.height = 5
            self.height += 1

        if self.rect.y > 515 + 64:
            self.y = 515 + 64
            self.height = 15
            self.fallcheck = False

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

        # Check for losing condition (player collides with enemy)
        for object in self.eng.scene.updateables:
            if isinstance(object, Enemy):
                if object.rect.x < self.rect.x + self.size and object.rect.x + self.size > self.rect.x:
                    if object.rect.y < self.rect.y + self.size and object.rect.y + self.size > self.rect.y:
                        print("Lose")
                        self.eng.screen.fill((0,0,0))
                        self.eng.screen.blit(self.failscreen, (0,0))
                        time.sleep(5)
                        self.eng.end()

class Score(DUGameObject):
    def __init__(self, eng):
        super().__init__()
        self.score = 0
        self.eng = eng
        self.image = pg.Surface((250,50))
        self.endscreen = pg.Surface((1000,1000))
        self.rect = self.image.get_rect()

    # Score is the same as number of seconds of game time
    def update(self):
        self.score = self.score + self.eng.deltaTime
        font = pg.font.Font('freesansbold.ttf', 32)
        text = font.render('Score: ' + str(int(round(self.score, 2) * 1000)), True, (0,0,200))
        textRect = text.get_rect()
        textRect.center = (0,0)
        self.eng.screen.blit(self.image, (0,0))
        self.eng.screen.blit(text, (10,10))
        # Win condition: Survive for 20 seconds
        if self.score >= 20:
            print("Win")
            self.eng.screen.fill((0,0,0))
            self.eng.screen.blit(self.endscreen, (0,0))
            time.sleep(5)
            self.eng.end()
        print("Score: " + str(self.score))

    def getScore(self):
        return self.score