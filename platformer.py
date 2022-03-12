import sys
sys.path.append("../CIS-376-Pygame-Engine")

from Engine import *
from Scene import *
from game_objects import *
from game import *
import pygame as pg

def main():
    s = Scene('Platformer', [], [])
    e = Engine('Midterm', s)
    z = Enemy()
    s.drawables.add(z)
    s.updateables.add(z)
    e.run()

main()