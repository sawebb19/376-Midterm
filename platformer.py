import sys
sys.path.append("../CIS-376-Pygame-Engine/")

from Engine import *
from Scene import *
from game_objects import *
from enemies import *
from player import *
import pygame as pg

def main():
    s = Scene('Platformer', [], [])
    e = Engine('Midterm', s)
    e.screen.blit(pg.image.load("./assets/map.png").convert_alpha(), (0,0))
    p = Player(e, x=10, y=515+64)
    s.drawables.add(p)
    s.updateables.add(p)
    z = Enemy(e, x=850, y=515)
    z2 = Enemy(e, x=805, y=355, lb=600, rb=950)
    z3 = Enemy(e, x=219, y=355, lb=74, rb=424)
    z4 = Enemy(e, x=512, y=195, lb=360, rb=660)
    s.drawables.add(z)
    s.updateables.add(z)
    s.drawables.add(z2)
    s.updateables.add(z2)
    s.drawables.add(z3)
    s.updateables.add(z3)
    s.drawables.add(z4)
    s.updateables.add(z4)
    score = Score(e)
    s.updateables.add(score)
    e.run("./assets/map.png")

main()