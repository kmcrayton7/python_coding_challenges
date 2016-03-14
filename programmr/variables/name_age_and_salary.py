# Write a program to ask the user for his/her name, age, and salary (double). Follow the input/output format. Following conversation should be displayed as output on screen, where you will enter the values of name,age and salary.

print "Hello. What is your name? "
name = raw_input()

print "Hi %s! How old are you? " % name
age = raw_input() 

print "So you're %s? How much do you make %s? " % (age, name)
salary = raw_input() 

print "Wow %s, you are set for life. " % name
