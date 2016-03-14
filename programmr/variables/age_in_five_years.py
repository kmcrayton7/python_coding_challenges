'''Ask the user for their name. Then display their name to prove that you can recall it. Ask them for their age. Then display what their age would be five years from now. Then display what their age would be five years ago.'''

print "What's your name?:"
name = raw_input("> ")
print name

print "What's your age?:"
age = raw_input("> ")
print age

in_five_years = int(age) + 5

five_years_ago = int(age) - 5

print "You will be %d years old in five years." % (in_five_years)

print "You were %d years old five years ago." % (five_years_ago)