from sys import exit
import random

class BecomingAPopstar(object):
    
    def __init__(self):
        print "So you want to become a Pop Star? Are you really sure that you have what it takes? \n We shall see." 
    
    def set_points(self):
        points = 0
        self.points = points
        print self.points
        
        
class Unknown(BecomingAPopstar):
    
    def paths(self):
        choices = {
            1: 'Cafes',
            2: 'YouTube Videos',
            3: 'Street Performer',
            4: 'Get a real job'
        }
        print 'You are just beginning your music career and there are so many paths to stardom, which do you take?'
        print "Enter a number from 1 - 4 to begin your journey to pop stardom."
        
        action = int(raw_input("> "))
        while True:
	        if action > 0 and action < 5:
		        break
	        else:
		        print 'Please try again' 
    	        action = int(raw_input("> "))
    	
        action = random.choice(choices.values())
        print action
       
        if (action == 'Cafes'):
            self.points = 10
        elif (action == 'YouTube Videos'):
            self.points = 7
        elif (action == 'Street Performer'):
            self.points = 3
        elif (action == 'Get a real job'):
            self.points = 0
        
        print 'You have %d points towards becoming a pop star' % self.points
        
        return 'discovered'
        
# class Discovered(Unknown):
# 
#      def paths(self):
#         actions = {
#             1: 'Talent Competition',
#             2: 'Background Singer',
#             3: 'County Fairs',
#             4: 'Band Breaks up'
#         }
#         print 'All your hard word is paying off because you have been discovered, what do you do next?'
#         print "Enter a number from 1 -4 to continue on your journey to pop stardom." 
# 
#       action = int(raw_input("> "))
#         while True:
# 	        if action > 0 and action < 5:
# 		        break
# 	        else:
# 		        print 'Please try again' 
#     	        action = int(raw_input("> "))
#     	
#         action = random.choice(choices.values())
#         print action
#        
#         if (action == 'Talent Competition'):
#             self.points += 10
#         elif (action == 'Background Singer'):
#             self.points += 7
#         elif (action == 'County Fairs'):
#             self.points += 3
#         elif (action == 'Band Breaks up'):
#             self.points += 0
#         
#         print 'You have %d points towards becoming a pop star' % self.points

mary = Unknown()
mary.set_points()
mary.paths()



# class HotNewArtist(BecomingAPopstar):
# 
#      def paths(self):
#         actions = {
#             1: 'Recording Contract',
#             2: 'Opening Act',
#             3: 'National Festivals',
#             4: 'Manager runs off with ALL the money'
#         }
#         print 'You are just beginning your music career and there are so many paths to stardom, which do you take?'
#         print "Enter a number from 1 -4 to begin your journey to pop stardom." 
#         action = int(raw_input("> "))
# 
# class PaidYourDues(BecomingAPopstar):
# 
#      def paths(self):
#         actions = {
#             1: 'Wins a Grammy',
#             2: 'Billboard Top Ten Album',
#             3: 'Concert Headliner',
#             4: 'You lose your voice'
#         }
#         print 'You are just beginning your music career and there are so many paths to stardom, which do you take?'
#         print "Enter a number from 1 -4 to begin your journey to pop stardom." 
#         action = int(raw_input("> "))
# 
# class AlmostThere(BecomingAPopstar):
# 
#      def paths(self):
#         actions = {
#             1: 'Writes an Oscar winning song',
#             2: 'Performs at the Grammy\'s',
#             3: 'Sells out stadiums',
#             4: 'You fall off the stage, break your neck, and DIE!'
#         }
#         print 'You are just beginning your music career and there are so many paths to stardom, which do you take?'
#         print "Enter a number from 1 -4 to begin your journey to pop stardom." 
#         action = int(raw_input("> "))
# 
# class PopStar(BecomingAPopstar):
# 
#   def total_score(self):
#         if (self.points >= 81):
#             print "You did it! Enjoy your life at the top!"
#         elif (self.points >= 61):
#             print "OOOHHHH...close but not close enough" 
#         elif (self.points >= 41):
#             print "Better lucj next time"   
#         elif (self.points >= 21):
#             print "Don't quit your day job!" 
#         elif (self.points >= 21):
#             print "LOSER!"   
#         exit(1)