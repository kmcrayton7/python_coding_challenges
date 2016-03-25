# 1. Put everything in one class
# 2. Make use of __init__ somewhere and instantiating a property or 2
# 3. Takes in user input
# 
# print "How many bottles of beer do you have?"
# 
# starting_bottles_of_beer = int(raw_input("> "))
# 
# print "%r bottles of beer on the wall,\n %r bottles of beer.\n Take one down,\n pass it around,\n %r bottles of beer on the wall." % (starting_bottles_of_beer, starting_bottles_of_beer, starting_bottles_of_beer - 1)
# print "----------------"
# 
# for each_bottle in range(starting_bottles_of_beer):
# 	starting_bottles_of_beer = starting_bottles_of_beer - 1
# 	if starting_bottles_of_beer == 0:
# 		print "No more bottles of beer on the wall."
# 	else: 
# 	    print "%r bottles of beer on the wall,\n %r bottles of beer.\n Take one down,\n pass it around,\n %r bottles of beer on the wall." % (starting_bottles_of_beer, starting_bottles_of_beer, starting_bottles_of_beer - 1)
# 	    print "----------------"

# Version 1: Put everything in one class
class Bottles(object):
    def starting_bottles_of_beer(self, number):
        print "How many bottles of beer do you have?"
        self.number = number
        print self.number

        print "%r bottles of beer on the wall,\n %r bottles of beer.\n Take one down,\n pass it around,\n %r bottles of beer on the wall." % (self.number, self.number, self.number - 1)
        print "----------------"

        for each_bottle in range(self.number -1, 0, -1):
	        self.each_bottle = each_bottle
	        self.each_bottle - 1
	        if self.each_bottle == 0:
		        print "No more bottles of beer on the wall."
	        else: 
	            print "%r bottles of beer on the wall,\n %r bottles of beer.\n Take one down,\n pass it around,\n %r bottles of beer on the wall." % (self.each_bottle, self.each_bottle, self.each_bottle - 1)
	            print "----------------"

twenty = Bottles()
twenty.starting_bottles_of_beer(20)

# Version 2: Make use of __init__ somewhere and instantiating a property or 2
class Bottles(object):
    def __init__(self, x):
        self.starting_bottles_of_beer = x
        
    def bottles_of_beer(self):
        print "How many bottles of beer do you have?"
        print (self.starting_bottles_of_beer)

        print "%r bottles of beer on the wall,\n %r bottles of beer.\n Take one down,\n pass it around,\n %r bottles of beer on the wall." % (self.starting_bottles_of_beer, self.starting_bottles_of_beer, self.starting_bottles_of_beer - 1)
        print "----------------"

        for each_bottle in range(self.starting_bottles_of_beer -1, 0, -1):
	        self.each_bottle = each_bottle
	        self.each_bottle - 1
	        if self.each_bottle == 0:
		        print "No more bottles of beer on the wall."
	        else: 
	            print "%r bottles of beer on the wall,\n %r bottles of beer.\n Take one down,\n pass it around,\n %r bottles of beer on the wall." % (self.each_bottle, self.each_bottle, self.each_bottle - 1)
	            print "----------------"

twenty = Bottles(20)
twenty.bottles_of_beer()

# Version 3: Takes in user input
print "How many bottles of beer do you have?"
starting_bottles_of_beer = int(raw_input("> "))
        
class Bottles(object):
        
    def bottles_of_beer(self):
        self.starting_bottles_of_beer = starting_bottles_of_beer
        print (self.starting_bottles_of_beer)

        print "%r bottles of beer on the wall,\n %r bottles of beer.\n Take one down,\n pass it around,\n %r bottles of beer on the wall." % (self.starting_bottles_of_beer, self.starting_bottles_of_beer, self.starting_bottles_of_beer - 1)
        print "----------------"

        for each_bottle in range(self.starting_bottles_of_beer -1, 0, -1):
	        self.each_bottle = each_bottle
	        self.each_bottle - 1
	        if self.each_bottle == 0:
		        print "No more bottles of beer on the wall."
	        else: 
	            print "%r bottles of beer on the wall,\n %r bottles of beer.\n Take one down,\n pass it around,\n %r bottles of beer on the wall." % (self.each_bottle, self.each_bottle, self.each_bottle - 1)
	            print "----------------"

twenty = Bottles()
twenty.bottles_of_beer()