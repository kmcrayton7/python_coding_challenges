# Make a simple numeric calculator. It should prompt the user for three numbers. Then add the numbers together and divide by 2. Display the result. Your program must support numbers with decimals and not just integers.

print "This is a simple calculator. Please enter 3 numbers."

first_number = raw_input("Enter first number: ")

second_number = raw_input("Enter second number: ")

third_number = raw_input("Enter third number: ")

total = float(first_number) + float(second_number) + float(third_number)

total = total / 2
print "(%s + %s + %s) / 2 is: %s" % (first_number, second_number, third_number, total)