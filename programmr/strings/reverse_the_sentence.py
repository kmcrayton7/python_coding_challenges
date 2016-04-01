# Write a program to reverse the sentence wordwise.

print 'Please enter a sentence and I will work my magic.'
sentence = raw_input('> ')

words = sentence.split()

sentence_rev = ' '.join(reversed(words))
print sentence_rev