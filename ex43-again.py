from random import randint
class Scene(object):
    def enter(self):
        print("Should not have been called.")
        print("Subclass it and implement enter")
        exit(0)

class CentralCorridor(Scene):
    def enter(self):
        print("Welcome to Gothons.")
        joke = input("> ")
        if joke != "tell a joke":
            print("You're dead")
            return "death"
        else:
            print("Good joke!")
            return 'laser_weapon_armory'

class Death(Scene):
    def enter(self):
        print("You're dead.")
        exit(0)

class LaserWeaponArmory(Scene):
    def enter(self):
        print("Enter code")
        guess = int(input("> "))
        code = randint(1,3)
        guesses = 0

        while guess != code and guesses < 3:
            print("BUZZEEDDDD")
            guesses += 1 
            guess = int(input("> "))
        
        if guess == code:
            print("Coreect")
            return 'finished'

        else:
            print("Failed")
            return 'death'

class Finished(Scene):
    def enter(self):
        print("Good job! You won.")
        exit(0)

class Map(object):
    def __init__(self, scenes, first_scene, last_scene):
        self.scenes = scenes
        self.first_scene = first_scene
        self.last_scene = last_scene

    def scene(self, scene_name):
        return self.scenes[scene_name]

class Engine(object):
    def play(self, map):
        next_scene = map.first_scene

        while next_scene != map.last_scene:
            next_scene_obj = map.scene(next_scene)
            next_scene = next_scene_obj.enter()

        next_scene_obj = map.scene(next_scene)
        next_scene_obj.enter()

map = Map({
    'central_corridor' : CentralCorridor(),
    'laser_weapon_armory' : LaserWeaponArmory(),
    'death' : Death(),
    'finished' : Finished()
}, 'central_corridor', 'finished')

game = Engine()
game.play(map)