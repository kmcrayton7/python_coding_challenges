# The user is asked for several pieces of information. Display it on the screen as a summary.

name = raw_input("What's your name?: ")
age = raw_input("How old are you?: ")
college = raw_input("What college do you attend?: ")
major = raw_input("What's your major?: ")

print "Hello %s, you told me that you are %s years old. You are currently attending %s and your major is %s." % (name, age, college, major)
