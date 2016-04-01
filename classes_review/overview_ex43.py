from sys import exit
from random import randint

class Scene(object):
    
    def enter(self):
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
        current_scene.enter()

class Death(Scene):

    quips = [
        'You died. You kinda suck at this.',
        'Your mom would be proud...if she were smarter.',
        'Such a luser.',
        'I have a small puppy that\'s better at this.'
    ]
    
    def enter(self):
        print Death.quips[randint(0, len(self.quips) -1)]
        exit(1)
        
class CentralCorridor(Scene):
    
    def enter(self):
        print 'The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew.\n' 
        print 'You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting into an escape pod.\n' 
        print 'You\'re running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume flowing around his filled body.\n'
        print 'He\'s blocking the door to the Armory and about to pull a weapon to blast you.'
        
        action = raw_input("> ")
        
        if action == 'shoot!':
            print 'Quick on the draw you yank out your blaster and fire at the Gothon\n.' 
            print 'His clown costume is flowing and moving around body, which throws off your aim\n.' 
            print 'Your laser hits his costume but misses him entirely. This completely ruins his brand new costume his mother bought him, which makes him fly into a insane rage and blast you repeatedly in the until you are dead\n.' 
            print 'Then he eats you.'
            return 'death'
            
        elif action == 'dodge!':
            print 'Like a world class boxer you dodge, weave, slip, and slide right as the Gothon\'s blaster cranks a laser past your head\n.'
            print 'In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out\n.'
            print 'You wake up shortly after only to die as the Gothon stomps on your head and eats you.'
            return 'death'

        elif action == 'tell a joke':
            print 'Lucky for you they made you learn Gothon insults in the academy\n.' 
            print 'You tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gut ubhfr\n.'
            print 'The Gothon stops, tries not to laugh, then busts out laughing and can\'t move\n.' 
            print 'While he\'s laughing you run up and shoot him in the head putting him down, then jump through the Weapon Armory door.'
            return 'laser_weapon_armory'
      
        else:
            print 'DOES NOT COMPUTE!'
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print 'You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding\n.' 
        print 'It\'s dead quiet, too quiet. You stand up and run to the far side of the room and find the neutron bomb in its container\n.'
        print 'There\'s a keypad lock on the box and you need the code to get the bomb out\n.' 
        print 'If you get the code wrong 10 times then the lock closes forever and you can\'t get the bomb\n.' 
        print 'The code is 3 digits.'
        
        code = '%d%d%d' % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = raw_input('[keypad]> ')
        guesses = 0

        while guess != code and guesses < 10:
            print 'BZZZEDDD!'

            guesses += 1
            guess = raw_input('[keypad]> ')
            
        if guess == code:
            print 'The container clicks open and the seal breaks, letting gas out\n.' 
            print 'You grab the neutron bomb and run as fast as you can to the bridge where you must place it in the right spot.'
            return 'the_bridge'

        else: 
            print 'The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together\n.' 
            print 'You decide tosit there, and finally the Gothons blow up the ship from their ship and you die.'
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print 'You burst onto the Bridge with the netron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of the ship\n.' 
        print 'Each of them has an even uglier clown costume than the last\n.' 
        print 'They haven\'t pulled their weapons out yet, as they see the acitve bomb under your arm and don\'t want to set it off.'
        
        action = raw_input("> ")
        
        if action == 'throw the bomb':
            print 'In a panic you throw the bomb at the group of Gothons and make a leap for the door\n.'
            print 'Right as you drop it a Gothon shoots you right in the back killing you\n.' 
            print 'As you die you see another Gothon frantically try to disarm the bomb. You die knowing they will probably blow up when it goes off.'
            return 'death'
    
        elif action == 'slowly place the bomb':
            print 'You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat\n.' 
            print 'You inch backward to the door, open it, and then carefully place the bomb on the floor, pointing your blaster at it\n.' 
            print 'You then jump back through the door, punch the close button and blast the lock so the Gothons can\'t get out\n.' 
            print 'Now that the bomb is placed you run to the escape pod to get off this tin can.'
            return 'escape_pod'

        else: 
            print 'DOES NOT COMPUTE!'
            return 'the_bridge'   

class EscapePod(Scene):
    
    def enter(self):
        print 'You rush through the ship despersately trying to make it to the escape pod before the whole ship explodes\n.' 
        print 'It seems like hardly any Gothons are on the ship, so your run is clear of interference\n.' 
        print 'You get to the chamber with the excape pods, and now need to pick one to take. Some of them could be damaged but you don\'t have time to look\n.' 
        print 'There\'s 5 pods, which one do you take?'

        good_pod = randint(1, 5)
        guess = raw_input('[pod #]>')

        if int(guess) != good_pod:
            print 'You jump into pod %s and hit the eject button. ' % guess
            print 'The pod escapes out into the void of space, then implodes as the hull ruptures, crushing your body into jam jelly.'
            return 'death'

        else:
            print 'You jump into pod %s and hit the eject button.' % guess
            print 'The pod easily slides out into space heading to the planet below\n.' 
            print 'As it flies to the planet, you look back and see your ship implode then explode like a bright star, taking out the Gothon ship at the same time. You won!'
            return 'finished'
           
class Finished(Scene):

    def enter(self):
        print 'You won! Good job.'
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