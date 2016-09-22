# python Documents\GitHub\gothons\gothons.py
""" Exercise 43 from Learn Python the Hard Way, called Gothons from Planet Percal #25.  Aliens have invaded a space ship
 and our hero has to go through a maze of rooms defeating them so he can escape into an escape pod to the planet below.
Each room will print its description when the player enters it and then tell the engine what room to run next out of the map.
Scenes:  Death something funny.
Central Corridor the starting point has a Gothon already standing there defeat with a joke before continuing.
Laser Weapon Armory where the hero gets a neutron bomb to blow up the ship before getting to the escape pod.
It has a keypad the hero has to guess the number for.
The Bridge Another battle scene with a Gothon where the hero places the bomb.
Escape Pod Where the hero escapes but only after guessing the right escape pod.
* Map
  - next_scene
  - opening_scene
* Engine
  - play
* Scene
  - enter
  * Death
  * Central Corridor
  * Laser Weapon Armory
  * The Bridge
  * Escape Pod
"""

# time.time() @ decorates a function with another function, so the first one runs inside the second

# import doctest
# doctest.testmod() returns None if all fake Python sessions in comments in this module do what they say (like so)
'''
>>> place_character(['  ', '  '], (0, 1), 'x')
['  ', 'x ']
'''

import pdb         # pdb.set_trace() stops everything and lets you do pdb commands
import traceback   # traceback.print_stack() just prints the stack at that point

from random import random, randint, seed

prompt = '> '

super_seed = randint(1,1000)
print "This seed is", super_seed
seed(super_seed)    # this will let you go back to good randomnesses

decay           = 0.8     # component branches die off by a power of this


class Grid(object):
    """The Grid is basically the screen or UI"""
    def __init__(self, width=winwidth, height=winheight, character=' '):
        self.grid = [[character for x in xrange(width)] for y in xrange(height)]

    def ischar(self, coordinate, character=' '):
        x, y = coordinate
        line = self.grid[y]
        if y < 0:                       # is this in the grid?
            return False
        if x < 0:
            return False
        if y >= len(self.grid):
            return False
        if x >= len(line):
            return False
        if line[x] == character:        # is it the thing?
            return True
        else:
            return False

stations.append(Station(outer_space, (0,0,'n'), {}))

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        print "welcome to Gothons from Planet Percal #25!  You're trapped on a Merchant Cruiser which has been overrun" \
              "by Gothon storm troopers.  They hate you and want to eat you.  Your only hope lies in finding the" \
              "Nukanuke in the Armory, setting it to detonate on the Bridge, and then finding an Escape Pod.  Good luck!"
        the_map.opening_scene()

class Scene(object):

    def enter(self):
        pass

class Death(Scene):

    def enter(self):
        while True:
            print "You've died aboard the ship!  Your body is quickly devoured by a Gothon and since Earth is destroyed" \
            "mere minutes later, no one remembers you.  Do you want to try again?"
            retry = raw_input(prompt)
            if retry == "yes" or "Yes" or "YES" or "y" or "N":
                return True
            elif retry == "no" or "No" or "NO" or "n" or "N":
                return False
            else:
                print "Sorry, what was that?"

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


the_map = Map('central_corridor')
the_game = Engine(a_map)
the_game.play()

# Do: make map._init_ build a map, starting with start_scene