import sys
sys.path.append("../CIS-376-Pygame-Engine/")

from Engine import *
from Scene import *
from game_objects import *
from enemies import *
from player import *
#from game import *
import pygame as pg

def main():
    s = Scene('Platformer', [], [])
    e = Engine('Midterm', s)
    z = Enemy(e, x=900, y=600)
    s.drawables.add(z)
    s.updateables.add(z)
    p = Player(e, y=600)
    s.drawables.add(p)
    s.updateables.add(p)
    e.run()

main()