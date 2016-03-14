''' 
Counting the number of a's:
Determine and print the number of times the character 'a' appears in the input entered by the user.
Example - Input: Enter String: This is a test; Output: Number of a's: 1
 '''

letters = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26, ' ' : 27}

print "Please write a short sentence here: " 
user_input = raw_input("> ")
letters = list(user_input)

# print list
# for letter_a in sentence:
# 	if letter_a == letters['a']:
# 		print 1 

print letters
