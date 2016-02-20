# bottles_of_beer = 99
# for each_bottle in range(100):
# 	bottles_of_beer = bottles_of_beer - 1
# 	print bottles_of_beer
# 	bottles_of_beer = bottles_of_beer--
# 	print "%r Bottles of beer on the wall." % bottles_of_beer


bottles_of_beer = 100
for each_bottle in range(99):
	bottles_of_beer = bottles_of_beer - 1
	bottles_left = bottles_of_beer -1
	print "%r bottles of beer on the wall,\n %r bottles of beer.\n Take 1 down, pass it around,\n %r bottles of beer on the wall." % (bottles_of_beer, bottles_of_beer, bottles_left)
