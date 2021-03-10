from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement later().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud... I guess.", 
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than a bad joke."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print("""
            The Gothons of Planet Percal #25 have invaded your ship and
            blah blah blah.

            You're running down the Central Corridor to the Weapons 
            Armory when a Gothon jumps out... He's blocking the door
            to the Armory and about to pull a weapon on you.
            """)

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                blah blah blah...he eats you.
                """))
            return 'death'
        
        elif action == "dodge!":
            print(dedent("""
                blah blah blah... he eats you.
                """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
            Lucky for you, blah blah blah... While he's laughing you
            shoot him and jump through the Weapon Armory door.
            """))
            return 'laser_weapon_armory'
        
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You do a dive roll in... You have 10 chances to unlock 
            the keypad to get the bomb blah blah blah. The code is
            3 digits.
            """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print(f'code is: {code}.')
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDD!")
            guesses += 1
            guess = input("[keypad]> ")
        
        if guess == code:
            print(dedent("""
                The container clicks open... grab bomb and run to
                bridge to place on right spot.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time... you die.
                """))
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You burst onto bridge with bomb blah blah blah
            Gothons don't want you to set off bomb.
            """))
        
        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                You panic, throw bomb, get shot and die.
                """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                Blah blah drama, place bomb, lock door and escape.
                """))
            return 'escape_pod'
        
        else:
            print('DOES NOT COMPUTE!')
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            Drama... There's 5 pods, which one do you take?
            """))

        good_pod = randint(1,5)
        print(f'Good pod is: {good_pod}.')
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
                You jump into pod {guess} and escape... but pod is
                damaged. You die.
                """))
            return 'death'

        else:
            print(dedent(f"""
                You jump into pod {guess} and escape... blah blah 
                blah... success. You won!
                """))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
