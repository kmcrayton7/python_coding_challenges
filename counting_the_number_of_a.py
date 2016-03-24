''' 
Counting the number of a's:
Determine and print the number of times the character 'a' appears in the input entered by the user.
Example - Input: Enter String: This is a test; Output: Number of a's: 1
 '''


how_many = {}
print "Please enter a line of text: " 
line = raw_input("> ")

letters = list(line)
print letters

for letter in letters:
    if letter == 'a':
        how_many[letter] = how_many.get(letter, 0) + 1

print how_many