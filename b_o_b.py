# version 1
bottles_of_beer = 100
for each_bottle in range(99):
	bottles_of_beer = bottles_of_beer - 1
	bottles_left = bottles_of_beer -1
	print "%r bottles of beer on the wall,\n %r bottles of beer.\n Take 1 down, pass it around,\n %r bottles of beer on the wall." % (bottles_of_beer, bottles_of_beer, bottles_left)

# version 2 
bottles_of_beer = 100
for each_bottle in range(99):
	bottles_of_beer = bottles_of_beer - 1
	bottles_left = bottles_of_beer -1
	print "%r bottles of beer on the wall,\n %r bottles of beer.\n Take 1 down, pass it around,\n %r bottles of beer on the wall." % (bottles_of_beer, bottles_of_beer, bottles_left)
        if bottles_left == 0:
		print "No more bottles of beer on the wall"

# version 3
print "How many bottles of beer do you have?"

starting_bottles_of_beer = int(raw_input("> "))

print "%r bottles of beer on the wall,\n %r bottles of beer.\n Take one down,\n pass it around,\n %r bottles of beer on the wall." % (starting_bottles_of_beer, starting_bottles_of_beer, starting_bottles_of_beer - 1)
print "----------------"

for each_bottle in range(starting_bottles_of_beer):
	starting_bottles_of_beer = starting_bottles_of_beer - 1
	if starting_bottles_of_beer == 0:
		print "No more bottles of beer on the wall."
	else: 
	    print "%r bottles of beer on the wall,\n %r bottles of beer.\n Take one down,\n pass it around,\n %r bottles of beer on the wall." % (starting_bottles_of_beer, starting_bottles_of_beer, starting_bottles_of_beer - 1)
	    print "----------------"