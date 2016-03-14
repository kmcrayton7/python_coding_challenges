# Ask the user to enter two variables 'a' and 'b'. Then assign the value of 'b-a +100' to 'b' and print values of both 'a' and 'b' as shown below.

 
value_a = int(raw_input("Enter a value for a: "))
value_b = int(raw_input("Enter a value for b: "))

value_b = value_b - value_a + 100 

print "a: %d" % value_a
print "b: %d" % value_b
