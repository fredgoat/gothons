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

class Map(object):

    def __init__(self, start_scene):
        self.spine = [start_scene]
        for x in xrange(randint(1,4)):
            self.spine.append([randint(1, 5), randint(1, 5)])
            self.spine[-1].insert(randint(0, 2), 0) # 0 is more corridor, 1-2 is deadend, 3-5 are side-scenes
        the_bridge = TheBridge()
        self.spine.append(the_bridge)
        while True:
            segment = randint(1,-2)
            direction = randint(0,2)
            if self.spine[segment][direction] == 0:
                pass
            else:
                self.spine[segment][direction] = 6  # 6 will be the armory
                break
        while True:
            segment = randint(1,-2)
            direction = randint(0,2)
            if self.spine[segment][direction] == 0 or 6:
                pass
            else:
                self.spine[segment][direction] = 7  # 7 will be the escape pods

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        self.spine[0].enter()

class Engine(object):

    def __init__(self, scene_map):
        self.map = scene_map
        self.location = (0,0) # 0 to whatever segment, 0-4 direction.  0 = main, 1 = left, 2 = forward, 3 = right

    def play(self):
        print "welcome to Gothons from Planet Percal #25!  You're trapped on a Merchant Cruiser which has been overrun " \
              "by Gothon storm troopers.  They hate you and want to eat you.  Your only hope lies in finding the " \
              "Nukanuke in the Armory, setting it to detonate on the Bridge, and then finding an Escape Pod."
        self.map.opening_scene()

    def forward(self):
        self.location = (self.location[0]+1,0)

    def backward(self):
        self.location = (self.location[0]-1,0)

    def left_turn(self):
        self.location = (self.location[0],1)

    def straight_turn(self):
        self.location = (self.location[0],2)

    def right_turn(self):
        self.location = (self.location[0],3)

class Scene(object):
    def __init__(self):
        self.items = []

    def enter(self):
        pass

class Death(Scene):

    def enter(self):
        while True:
            print "You've died aboard the ship!  Your body is quickly devoured by a Gothon and since Earth is destroyed " \
            "mere minutes later, no one remembers you.  Do you want to try again?"
            retry = raw_input(prompt)
            if retry.lower() in ("yes", "y"):
                print "Well, then restart or whatever."
                break
            elif retry.lower() in ("no", "n"):
                print "Okay, bye."
                break
            else:
                print "Sorry, what was that?"

class CentralCorridor(Scene):
    def __init__(self):
        self.items = ["a Gothon soldier"]

    def enter(self):
        print "You find yourself at the end of a relatively wide central corridor with many twists and branches, " \
        "running the length of the ship."
        if "a Gothon soldier" in self.items:
            print "A Gothon soldier, rounding the corner of the corridor, freezes for a second as it spots you.  What do you do?"
            response = raw_input(prompt)
            if response.lower() in ("punch", "punch it", "punch soldier", "punch gothon"):
                print "You punch it and it dies!"
                self.items.remove("a Gothon soldier")
                self.enter()
            else:
                print "What are you even trying to do?  It shoots, eats, and leaves.  You're dead now, and inside a Gothon."
                death = Death()
                death.enter()
        else:
            for x in self.items:
                print "You see %s here." % (x)
            print "There's only one way to go, here.  Are you ready to go forward?"
            response = raw_input(prompt)
            if response.lower() in ("forward", "go forward", "y", "yes"):
                the_game.forward()
            else:
                Print "Fine whatever, you die of starvation."
                death = Death()
                death.enter()

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

central_corridor = CentralCorridor()
the_map = Map(central_corridor)
the_game = Engine(the_map)
the_game.play()

# Do: What happens when you go forward from the corridor?