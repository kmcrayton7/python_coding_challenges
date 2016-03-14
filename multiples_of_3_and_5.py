'''
Multiples of 3 and 5:
Example: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Challenge: Find the sum of all the multiples of 3 or 5 below 1000.
'''
multiples_of_3 = 0
multiples_of_5 = 0
for number in range(1000):
	if number % 3 == 0:
		multiples_of_3 = number  
		print multiples_of_3
	elif number % 5 == 0:
		multiples_of_5 = number
		print multiples_of_5
	
		
# version 2 multiples of 3, 5, and 3 & 5
multiples_of_3 = 0
multiples_of_5 = 0
for number in range(1000):
	if number % 3 == 0:
		multiples_of_3 = number  
		print multiples_of_3
	elif number % 5 == 0:
		multiples_of_5 = number
		print multiples_of_5
	elif number % 3 ==0 and number % 5 ==0:
		multiples_of_3_and_5 = number
		print multiples_of_3_and_5
		
# version 3 starting with empty arrays and append multiples of 3 or 5
multiples_of_3 = []
multiples_of_5 = []
for number in range(1000):
	if number % 3 == 0:
		multiples_of_3 == number
		multiples_of_3.append(number)
		
print multiples_of_3
for number in range(1000):
	if number % 5 == 0:
		multiples_of_5 == number
		multiples_of_5.append(number)
		
print multiples_of_5

# version 4
multiples_of_3 = []
multiples_of_5 = []
for number in range(1000):
	if number % 3 == 0:
		multiples_of_3 == number
		multiples_of_3.append(number)
		
	if number % 5 == 0:
		multiples_of_5 == number
		multiples_of_5.append(number)
		
print multiples_of_3, multiples_of_5