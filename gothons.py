# python Documents\GitHub\gothons\gothons.py
""" Exercise 43 from Learn Python the Hard Way, called Gothons from Planet Percal #25.  Aliens have invaded a space ship
 and our hero has to go through a maze of rooms defeating them so he can escape into an escape pod to the planet below.
Each room will print its description when the player enters it and then tell the engine what room to run next out of
the map.
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
  the_game.movement is a tuple that gives ship segment and turn (main, left, forward, right) whereas the_map.spine is
   a list (the segments) of lists (forward, left, right) of rooms, plus special locations at the beginning and end
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

super_seed = randint(1, 1000)
print "This seed is", super_seed
seed(super_seed)    # this will let you go back to good randomnesses


class Map(object):

    def __init__(self, start_scene):
        self.spine = [start_scene]
        for x in xrange(randint(1, 4)):  # append 1-4 random ship segments
            self.spine.append([randint(1, 5), randint(1, 5)])  # 0 is more corridor, 1-2 is deadend, 3-5 are side-scenes
            self.spine[-1].insert(randint(0, 2), 0)  # append a corridor (0) 0 is forward, 1 is left, 2 is right
        self.spine.append(the_bridge)  # append the bridge
        while True:
            segment = randint(1, len(self.spine)-2)  # pick a segment, but not the first (the start) or last (bridge)
            direction = randint(0, 2)  # pick a direction
            if self.spine[segment][direction] == 0:
                pass
            else:
                self.spine[segment][direction] = 6  # if it's not part of the corridor, it will be the armory (6)
                break
        while True:
            segment = randint(0, 3)-2
            direction = randint(0, 2)
            if self.spine[segment][direction] == 0 or 6:
                pass
            else:
                self.spine[segment][direction] = 7  # if it's not corridor or armory, it will be the pods (7)
                break

    def reset(self):
        the_game.movement = (the_game.movement[0],0)
        the_game.map.next_scene()

    def next_scene(self):
        segment = self.spine[the_game.movement[0]]  # you're at whatever segment you moved to
        if the_game.movement[1] == 0:  # if you went forward or backward along the main corridor
            if segment == the_bridge:
                the_bridge.enter()
            elif segment == central_corridor:
                central_corridor.enter()
            else:
                while True:
                    print "You continue down the twisting corridor, until it branches, then reorient yourself from" \
                          " whence you began.  Which way do you go?"
                    move = raw_input(prompt)
                    if move.lower() in ("f", "s", "go forward", "forward", "go straight", "straight", "a", "ahead",
                                        "keep going"):
                        if segment[0] == 0:
                            the_game.forward()
                            break
                        else:
                            the_game.straight_turn()
                            break
                    elif move.lower() in ("l", "left", "turn left", "go left"):
                        if segment[1] == 0:
                            the_game.forward()
                            break
                        else:
                            the_game.left_turn()
                            break
                    elif move.lower() in ("r", "right", "right turn", "go right"):
                        if segment[2] == 0:
                            the_game.forward()
                            break
                        else:
                            the_game.right_turn()
                            break
                    else:
                        print "What?"
        elif the_game.movement[1] == 1 or 2 or 3:  # if you turned off the main corridor
            direc = the_game.movement[1]
            if direc == 2:
                direc = 0
            if segment[direc] == 1 or 2:
                print "Oops!  It's just a dead-end!  You'd better hurry!  You return to the main corridor and" \
                      " reorient yourself."
                the_map.reset()
            elif segment[direc] == 3:
                print "You stumble into a merchant barracks which several dozing Gothon soldiers are using as such." \
                      "  Quietly, you back out to the main corridor and reorient."
                the_map.reset()
            elif segment[direc] == 4:
                print "Ship stores!  You pig out on algaesnax for a minute, and then return to the task at hand."
                the_map.reset()
            elif segment[direc] == 5:
                print "Maintenance closet!  You trip over some wires that look important, but the ship doesn't explode"
                the_map.reset()
            elif segment[direc] == 6:
                the_armory.enter()
            elif segment[direc] == 7:
                the_pods.enter()
            else:
                print "Somehow you wandered out of an airlock!  Space death!"
                airlock = Death()
                airlock.enter()

    def opening_scene(self):
        self.spine[0].enter()


class Engine(object):

    def __init__(self, scene_map):
        self.map = scene_map
        self.movement = (0, 0)  # 0 to whatever segment, 0-4 direction.  0 = main, 1 = left, 2 = forward, 3 = right

    def play(self):
        print "welcome to Gothons from Planet Percal #25!  You're trapped on a Merchant Cruiser which has been" \
              " overrun by Gothon storm troopers.  They hate you and want to eat you.  Your only hope lies in finding" \
              " the Nukanuke in the Armory, setting it to detonate on the Bridge, and then finding an Escape Pod."
        self.map.opening_scene()

    def forward(self):
        self.movement = (self.movement[0] + 1, 0)
        the_game.map.next_scene()

    def backward(self):
        self.movement = (self.movement[0] - 1, 0)
        the_game.map.next_scene()

    def left_turn(self):
        self.movement = (self.movement[0], 1)
        the_game.map.next_scene()

    def straight_turn(self):
        self.movement = (self.movement[0], 2)
        the_game.map.next_scene()

    def right_turn(self):
        self.movement = (self.movement[0], 3)
        the_game.map.next_scene()


class Scene(object):
    def __init__(self):
        self.items = []

    def enter(self):
        pass


class Death(Scene):

    def enter(self):
        while True:
            print "You've died aboard the ship!  Your body is quickly devoured by a Gothon and since Earth is" \
                  " destroyed mere minutes later, no one remembers you.  Do you want to try again?"
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
            print "A Gothon soldier, rounding the corner of the corridor, freezes for a second as it spots you." \
                  "  What do you do?"
            response = raw_input(prompt)
            if response.lower() in ("punch", "punch it", "punch soldier", "punch gothon"):
                print "You punch it and it dies!"
                self.items.remove("a Gothon soldier")
                self.enter()
            else:
                print "What are you even trying to do?  It shoots, eats, and leaves.  You're dead now, and inside" \
                      " a Gothon."
                shot = Death()
                shot.enter()
        else:
            for x in self.items:
                print "You see %s here." % x
            print "There's only one way to go, here.  Are you ready to go forward?"
            response = raw_input(prompt)
            if response.lower() in ("forward", "go forward", "y", "yes"):
                the_game.forward()
            else:
                print "Fine whatever, you die of starvation."
                no_go = Death()
                no_go.enter()


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You find a big metal door that the merchants probably used to secure something really dangerous.  " \
              "It has yellow hazard chevrons on it and everything.  As you approach, the door starts to open."
        response = raw_input(prompt)
        if response.lower() in ("hide", "crouch", "duck", "sneak"):
            print "You duck behind a support beam just as the Gothon walks out.  It turns and punches something " \
                  "into the keypad.  You hear five monotone beeps and the sound of a lock clicking into place.  " \
                  "Then the Gothon walks off, luckily without noticing you."
            while True:
                print "What now?"
                response = raw_input(prompt)
                if response.lower() in ("try the keypad", "try keypad", "keypad", "use the keypad", "use keypad",
                                        "unlock keypad", "unlock the keypad", "unlock", "type", "hack the keypad",
                                        "hack keypad"):
                    tries = 7
                    while tries > 0:
                        print "You try to guess the keypad sequence.  What do you press?"
                        response = raw_input(prompt)
                        tries -= 1
                        if response == str(code*11111):
                            print "Miraculously, you guess the combo!  You're in.  It's a Laser Weapon Armory!  " \
                                  "You grab a multibeam and are about to leave when you notice a Nukanuke.  It's " \
                                  "small enough to carry.  Do you take it?"
                            response = raw_input(prompt)
                            if response.lower() in ("y", "yes", "yeah", "take", "take it", "take the nukanuke",
                                                    "take nukanuke"):
                                print "You grab that thing and head back to the main corridor."
                                global nuke
                                nuke = 1
                                the_map.reset()
                            else:
                                print "Your equivocation disgusts me.  You lose and die."
                                no_nukes = Death()
                                no_nukes.enter()
                        else:
                            print "Your button mashing is useless!  You hear footsteps!  Better guess again, and fast!"
                    print "Oh no!  The Gothon returned!  It slices you into hamburger with its claws!"
                    sliced = Death()
                    sliced.enter()
                    break
                elif response.lower() in ("leave", "go back", "return", "return to corridor", "turn back"):
                    print "You head back to the main corridor."
                    the_map.reset()
                    break
                else:
                    "I didn't catch that."
        else:
            print "Oops!  The Gothon coming through the door totally caught you.  It growls at you, and you die " \
                  "from an aneurysm."
            aneurysm = Death()
            aneurysm.enter()


class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        pass

nuke = 0
code = randint(0, 9)
pod = randint(1, 3)
the_armory = LaserWeaponArmory()
the_bridge = TheBridge()
the_pods = EscapePod()
central_corridor = CentralCorridor()
the_map = Map(central_corridor)
the_game = Engine(the_map)
the_game.play()

# Do: Bridge battle and nuking, and escape pod guessing scenes!  Try it out!
