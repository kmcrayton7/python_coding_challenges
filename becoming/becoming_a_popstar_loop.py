from sys import exit
import random

class BecomingAPopstar(object):
    
    def __init__(self):
        points = 0
        self.points = points
    
    def career_paths(self):
        return Unknown()
        
class Unknown(BecomingAPopstar):

    def career_paths(self):
        choices = {
            1: 'Cafes',
            2: 'YouTube Videos',
            3: 'Street Performer',
            4: 'Get a real job'
        }
        print 'You are just beginning your music career and there are so many paths to stardom, which once do you take?\n'
        print "Enter a number from 1 - 4 to begin your journey to pop stardom.\n"
        
        action = int(raw_input("> "))
        while True:
	        if action > 0 and action < 5:
		        break
	        else:
		        print 'Please try again\n' 
    	        action = int(raw_input("> "))
    	
        action = random.choice(choices.values())
        print action
       
        if (action == 'Cafes'):
            self.points = 10
            print 'Singing in cafes earns you 10 points\n'
        elif (action == 'YouTube Videos'):
            self.points = 7
            print 'Creating YouTube videos earns you 7 points\n'
        elif (action == 'Street Performer'):
            self.points = 3
            print 'Being a street performer earns you 3 points\n'
        elif (action == 'Get a real job'):
            self.points = 0
            print 'Having to get a job earns you 0 points'
        print 'You now have %d points towards becoming a pop star\n' % self.points
        
        return Discovered()
        
class Discovered(BecomingAPopstar):

     def career_paths(self):
        choices = {
            1: 'Reality Talent Competition',
            2: 'Background Singer',
            3: 'County Fairs',
            4: 'Band Breaks up'
        }
        print 'All your hard work is paying off because you have been discovered, what path do you take next?\n'
        print "Enter a number from 1 - 4 to continue on your journey to pop stardom.\n" 

        action = int(raw_input("> "))
        while True:
	        if action > 0 and action < 5:
		        break
	        else:
		        print 'Please try again' 
    	        action = int(raw_input("> "))
    	        
    	action = random.choice(choices.values())
        print action       
     
        if (action == 'Reality Talent Competition'):
            self.points += 10
            print 'Being on a reality show talent cometition earns you 10 points\n'
        elif (action == 'Background Singer'):
            self.points += 7
            print 'Becoming a background singer earns you 7 points\n'
        elif (action == 'County Fairs'):
            self.points += 3
            print 'Performing at county fairs earns you 3 points\n'
        elif (action == 'Band Breaks up'):
            self.points += 0
            print 'Your bands breaks up which earns you 0 points\n'
        
        print 'You have %d points towards becoming a pop star\n' % self.points
        
        return HotNewArtist()

class HotNewArtist(BecomingAPopstar):

    def career_paths(self):
        choices = {
            1: 'Recording Contract',
            2: 'Opening Act',
            3: 'National Festivals',
            4: 'You lose your voice'
        }
        print 'You are one step closer...you are the latest hot new artist. What path will you take now?\n'
        print "Enter a number from 1 - 4 to begin your journey to pop stardom.\n" 
        
        action = int(raw_input("> "))
        while True:
	        if action > 0 and action < 5:
		        break
	        else:
		        print 'Please try again' 
    	        action = int(raw_input("> "))
    	        
    	action = random.choice(choices.values())
        print action       
     
        if (action == 'Recording Contract'):
            self.points += 10
            print 'You\'ve signed a recording contract which earns you 10 points\n'
        elif (action == 'Opening Act'):
            self.points += 7
            print 'You\'re the opening act for to current Pop Star which earns you 7 points\n'
        elif (action == 'National Festivals'):
            self.points += 3
            print 'Singing at international music festivals earns you 3 points\n'
        elif (action == 'You lose your voice'):
            self.points += 0
            print 'Losing your voice earns you 0 points\n'
            
        print 'You have %d points towards becoming a pop star\n' % self.points
        
        return PaidYourDues()

class PaidYourDues(BecomingAPopstar):

     def career_paths(self):
        choices = {
            1: 'Wins a Grammy',
            2: 'Billboard Top Ten Album',
            3: 'Concert Headliner',
            4: 'Manager runs off with ALL the money'
        }
        print 'So, you\'ve paid your dues and are finally getting some recognition. What path will lead to more fame?\n'
        print "Enter a number from 1 - 4 to begin your journey to pop stardom.\n" 
        
        action = int(raw_input("> "))
        while True:
	        if action > 0 and action < 5:
		        break
	        else:
		        print 'Please try again' 
    	        action = int(raw_input("> "))
    	        
    	action = random.choice(choices.values())
        print action       
     
        if (action == 'Wins a Grammy'):
            self.points += 10
            print 'Winning a Grammy earns you 10 points\n'
        elif (action == 'Billboard Top Ten Album'):
            self.points += 7
            print 'Having a Top 10 on the Billboard charts earns you 7 points\n'
        elif (action == 'Concert Headliner'):
            self.points += 3
            print 'Headlining your own concert earns you 3 points'
        elif (action == 'Manager runs off with ALL the money'):
            self.points += 0
            print 'And of course, having your manager run off with your money earns you 0 points\n'
            
        print 'You have %d points towards becoming a pop star\n' % self.points

        return AlmostThere()
        
class AlmostThere(BecomingAPopstar):

     def career_paths(self):
        choices = {
            1: 'Writes an Oscar winning song',
            2: 'Performs at the Grammy\'s',
            3: 'Sells out stadiums',
            4: 'You fall off the stage, break your neck, and DIE!'
        }
        print 'WOW! Congratulations! You are at the top of your game. All roads lead to Pop Stardom...are do they?\n'
        print "Enter a number from 1 -4 to begin your journey to pop stardom.\n" 
        
        action = int(raw_input("> "))
        while True:
	        if action > 0 and action < 5:
		        break
	        else:
		        print 'Please try again' 
    	        action = int(raw_input("> "))
    	        
    	action = random.choice(choices.values())

     
        if (action == 'Writes an Oscar winning song'):
            self.points += 10
            print 'Writing an Oscar winning song earns you 10 points\n'
        elif (action == 'Performs at the Grammy\'s'):
            self.points += 7
            print 'Performing at the Grammy\'s earns you 7 points\n'
        elif (action == 'Sells out stadiums'):
            self.points += 3
            print 'Selling out a 20,000 stadium earns you 3 points'
        elif (action == 'You fall off the stage, break your neck, and DIE!'):
            self.points *= 0
            print 'OOPS...you break your neck and die after falling off the stage which earns you 0 points\n'
        
        print 'You have %d points towards becoming a pop star\n' % self.points

        if (self.points >= 41):
            print "You did it! Enjoy your life at the top!\n"
        elif (self.points >= 31):
            print "OOOHHHH...close but not close enough.\n" 
        elif (self.points >= 21):
            print "Better luck next time.\n"   
        elif (self.points >= 11):
                print "Don't quit your day job!\n" 
        else:
            print "LOSER!"   
        exit(1)

def main():
    level_classes = [ Unknown, Discovered, HotNewArtist, PaidYourDues, AlmostThere ]
    print "So you want to become a Pop Star? Are you really sure that you have what it takes? We shall see. It takes 41 points or more to become a Pop Star.\n"
    
    last_level = None
    for level_class in level_classes:
        level = level_class()
        if last_level != None:
            level.points = last_level.points
        level.career_paths()
        last_level = level
    
main()
