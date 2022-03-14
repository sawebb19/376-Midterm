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
    p = Player(e, x=10, y=515)
    s.drawables.add(p)
    s.updateables.add(p)
    z = Enemy(e, x=850, y=515)
    s.drawables.add(z)
    s.updateables.add(z)
    score = Score(e)
    s.updateables.add(score)
    e.run()

main()