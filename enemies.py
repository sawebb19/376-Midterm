import sys
sys.path.append("../CIS-376-Pygame-Engine")

from Engine import *
from Scene import *
from game_objects import *

class Enemy(DUGameObject):
    def __init__(self, x=0, y=0):
        super.__init__()
        self.dirty = 2
        self.direction = 0
        self.speed = 0
        self.x = x
        self.y = y
        self.walk_time = 0
        self.current_frame = 0

    # TODO
    def update(self):
        pass
        # Zombie code that might be helpful for walking
        
        # self.walk_time = self.walk_time + Engine.Engine.delta_time
        #     if self.walk_time > .1:
        #         self.current_frame = (self.current_frame + 1 ) % 10
        #         self.walk_time = 0
        #     self.image = self.images[self.direction][self.current_frame]
        #     dir = 1
        #     if self.direction == 1:
        #         dir = -1
        #     self.x = self.x + 100 * Engine.Engine.delta_time * dir  * self.speed
        #     self.rect.x = self.x
        #     self.rect.y = self.y
        #     for event in Engine.Engine.events:
        #         if event.type == pg.KEYDOWN:
        #             if event.key == pg.K_a:
        #                 self.direction = 1
        #             if event.key == pg.K_d:
        #                 self.direction = 0
        #                 self.image = pg.transform.flip(self.image, True, False)
        #     pg.draw.rect(self.image, (0, 0, 255), self.image.get_bounding_rect(), width=1)
        #     pg.draw.rect(self.image, (255, 0, 0), self.image.get_rect(), width=1)
