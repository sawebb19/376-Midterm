import sys
sys.path.append("../CIS-376-Pygame-Engine")

from Engine import *
from Scene import *
from game_objects import *
from game import *

def main():
    s = Scene('scene1', [], [])
    e = Engine('assignment1', s)
    z = Zombie()
    s.drawables.add(z)
    s.updateables.add(z)
    e.run()

main()