# Write a program which prints the factors of a given number.
# Example - Input: 6; Output: 1, 2, 3, 6
# Example - Input: 10; Output: 1, 2, 5, 10
	 
# version 1: the code works
print "This program is designed to return all the factors of a number."
print "Factors are the numbers that a larger number can be divided by."
print "\n"

print "Give me a number:" 

your_number = int(raw_input("> "))

print "Your number is: %r" % (your_number)

for factor in range( 1, your_number):
	factors = your_number % factor == 0
	if factors == True:
		print factor
	else:
		print ""
print your_number

# version 2: figured how to print True without the spaces for False
print "This program is designed to return all the factors of a number."
print "Factors are the numbers that a larger number can be divided by."
print "\n"

print "Give me a number:" 

your_number = int(raw_input("> "))

print "Your number is: %r" % (your_number)

for factor in range( 1, your_number):
	factors = your_number % factor == 0
	if factors == True:
		print factor
print your_number