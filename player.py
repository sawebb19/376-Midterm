import sys
sys.path.append("../CIS-376-Pygame-Engine")

from Engine import *
from Scene import *
from game_objects import *

class Player(DUGameObject):
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

# TODO - having a camera tied to the player should be easier to manage
class Camera(UGameObject):
    pass