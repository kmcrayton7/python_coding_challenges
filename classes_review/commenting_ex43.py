from sys import exit
from random import randint

# creates a Scene class which inherits from the Python object class
class Scene(object):
    
    # creates a enter method which takes self as its first parameter which will allow objects to access it
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        # calls exit with the param 1
        exit(1)

# creates a Engine class which inherits from the Python object class        
class Engine(object):
    
    # __init__ method ensures that the code inside gets called as soon as an Engine class is instantiated. It takes scene_map as a second param.
    def __init__(self, scene_map):
        # every Engine object/instance has its own scene_map
        self.scene_map = scene_map
    
    # play method sets where the player is in the game
    def play(self):
        # current_scene is set to the scene map with the method opening scene
        current_scene = self.scene_map.opening_scene()
        # last scene is set to scene map with the method next scene with finished passed in as the param
        last_scene = self.scene_map.next_scene('finished')
        
        # while the current scene is not the last scene
        while current_scene != last_scene:
            # next scene name is set to the name of the enter method of the current scene
            next_scene_name = current_scene.enter()
            # current scene is set to scene map with the method next scene with next scene name passed in as a param
            current_scene = self. scene_map.next_scene(next_scene_name)
        # calls the enter method based on the current scene
        current_scene.enter()

# creates a Death class which inherits from the Scene class
class Death(Scene):
    
    # quips is an attribute of the class Death
    quips = [
        'You died. You kinda suck at this.',
        'Your mom would be proud...if she were smarter.',
        'Such a luser.',
        'I have a small puppy that\'s better at this.'
    ]
    #creates a enter method
    def enter(self):
        # prints the attribute quips based on a random number from 0 through the length of quips -1
        print Death.quips[randint(0, len(self.quips) -1)]
        exit(1)
        
# creates a CentralCorridor class which inherits from the Scene class
class CentralCorridor(Scene):
    
    #creates a enter method
    def enter(self):
        print '''The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew. You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting into an escape pod. \n You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume flowing around his filled body. He's blocking the door to the Armory and about to pull a weapon to blast you.'''
        
        # the action attribute is set to the user's input
        action = raw_input("> ")
        
        # if action is equal to 'shoot'
        if action == 'shoot!':
            print '''Quick on the draw you yank out your blaster and fire at the Gothon. His clown costume is flowing and moving around body, which throws off your aim. Your laser hits his costume but misses him entirely. This completely ruins his brand new costume his mother bought him, which makes him fly into a insane rage and blast you repeatedly in the until you are dead. Then he eats you.'''
            # calls the Death class and ends the game
            return 'death'
        
        # if action is equal to 'dodge'
        elif action == 'dodge!':
            print '''Like a world class boxer you dodge, weave, slip, and slide right as the Gothon's blaster cranks a laser past your head. In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out. You wake up shortly after only to die as the Gothon stomps on your head and eats you.'''
            # calls the Death class and ends the game
            return 'death'
        # if action is equal to 'tell a joke'
        elif action == 'tell a joke':
            print '''Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gut ubhfr. The Gothon stops, tries not to laugh, then busts out laughing and can't move. While he's laughing you run up and shoot him in the head putting him down, then jump through the Weapon Armory door.'''
            
            #call the laser weapons armory scene
            return 'laser_weapon_armory'
        # if all of the above fail do this 
        else:
            print 'DOES NOT COMPUTE!'  
            # returns the player to the central corridor 
            return 'central_corridor'
        
# creates a LaserWeaponArmory class which inherits from the Scene class
class LaserWeaponArmory(Scene):
    
    #creates a enter method
    def enter(self):
        print '''You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding. It's dead quiet, too quiet. You stand up and run to the far side of the room and find the neutron bomb in its container. There's a keypad lock on the box and you need the code to get the bomb out. If you get the code wrong 10 times then the lock closes forever and you can't get the bomb. The code is 3 digits.'''
        # code is set to 3 random numbers from 1 to 9
        code = '%d%d%d' % (randint(1, 9), randint(1, 9), randint(1, 9))
        # guess is set to the user input saved in the code attribute
        guess = raw_input('[keypad]> ')
        
        #guesses is set to 0
        guesses = 0
        
        # while guess is not equal to code and guesses is less then 10:
        while guess != code and guesses < 10:
            print 'BZZZEDDD!'
            
            #increment guesses by 1 for each time through the loop
            guesses += 1
            # guess is set to the user input saved in the code attribute
            guess = raw_input('[keypad]> ')
        
        # if guess is equal to code
        if guess == code:
            print '''The container clicks open and the seal breaks, letting gas out. You grab the neutron bomb and run as fast as you can to the bridge where you must place it in the right spot.'''
            # returns the player to the bridge
            return 'the_bridge'
            
        # otherwise you die
        else: 
            print '''The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together. You decide tosit there, and finally the Gothons blow up the ship from their ship and you die.'''
            # calls the Death class and ends the game
            return 'death'
        
# creates a TheBridge class which inherits from the Scene class
class TheBridge(Scene):
    
    #creates a enter method
    def enter(self):
        print '''You burst onto the Bridge with the netron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of the ship. Each of them has an even uglier clown costume than the last. They haven't pulled their weapons out yet, as they see the acitve bomb under your arm and don't want to set it off.'''
        
        # the action attribute is set to the user's input
        action = raw_input("> ")
        
        # if action is equal to 'throw the bomb'
        if action == 'throw the bomb':
            print '''In a panic you throw the bomb at the group of Gothons and make a leap for the door. Right as you drop it a Gothon shoots you right in the back killing you. As you die you see another Gothon frantically try to disarm the bomb. You die knowing they will probably blow up when it goes off.'''
            return 'death'
        
        # if action is equal to 'slowly place the bomb'    
        elif action == 'slowly place the bomb':
            print '''You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat. You inch backward to the door, open it, and then carefully place the bomb on the floor, pointing your blaster at it. You then jump back through the door, punch the close button and blast the lock so the Gothons can't get out. Now that the bomb is placed you run to the escape pod to get off this tin can.'''
            # returns the player to the escape pod
            return 'escape_pod'
        # otherwise the player hasn't entered the correct response and is return back to the start of the bridge scene 
        else: 
            print 'DOES NOT COMPUTE!'
            return 'the_bridge'   
        
# creates a EscapePod class which inherits from the Scene class
class EscapePod(Scene):
    
    #creates a enter method
    def enter(self):
        print '''You rush through the ship despersately trying to make it to the escape pod before the whole ship explodes. It seems like hardly any Gothons are on the ship, so your run is clear of interference. You get to the chamber with the excape pods, and now need to pick one to take. Some of them could be damaged but you don't have time to look. There's 5 pods, which one do you take?'''
        
        # good pod is set to a random number from 1 to 5
        good_pod = randint(1, 5)
        
        # guess is set to the use's input
        guess = raw_input('[pod #]>')
        
        # if player's guess, which is being converted from a string to an integer, is not the good pod
        if int(guess) != good_pod:
            # the player's guess replaces %s
            print 'You jump into pod %s and hit the eject button. ' % guess
            print '''The pod escapes out into the void of space, then implodes as the hull ruptures, crushing your body into jam jelly.'''
            # calls the Death class and ends the game
            return 'death'
        # otherwise the player chooses a working pod and escapes successfully and is returned to the finished class 
        else:
            print 'You jump into pod %s and hit the eject button.' % guess
            print '''The pod easily slides out into space heading to the planet below. As it flies to the planet, you look back and see your ship implode then explode like a bright star, taking out the Gothon ship at the same time. You won!'''
            # calls the Finished class and ends the game
            return 'finished'

# creates a Finished class which inherits from the Scene class            
class Finished(Scene):
    
    #creates a enter method
    def enter(self):
        print 'You won! Good job.'
        # calls the Finished class and ends the game
        return 'finished'

# creates a Map class which inherits from Python's object class      
class Map(object):
    
    #creates a dictionary of the games scenes
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }
    
    # __init__ method ensures that the code inside gets called as soon as an Map class is instantiated. It takes start_scene as a second param.
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    # creates a next_scene method that takes scene_name as a second param.
    def next_scene(self, scene_name):
        # val is set to get the next scene's name
        val = Map.scenes.get(scene_name)
        # and return the next scene
        return val
    
    #creates a opening_scene method
    def opening_scene(self):
        # returns the start scene as the next scene to start the game
        return self.next_scene(self.start_scene)

# creates an instance of the Map class that takes central_corridor as a param and sets it equal to the variable a_map
a_map = Map('central_corridor')
# creates an instance of the Engine class that takes the object a_map as a param and sets if equal to the variable a_game
a_game = Engine(a_map)
# calls the play method on the object a_game
a_game.play()