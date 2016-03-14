'''
Pattern of Numbers
Write a program to print patterns as shown below:
Input: Enter the limit: 3 Output: 1, 12, 123
Input: enter the limit: 5 Output: 1, 12, 123, 1234, 12345
'''

# sum = 0
# pattern_of_numbers = ''
# for number in range(3):
# 	sum = sum + number
# 	print(str(pattern_of_numbers) + str(number))
# 	
# print "sum is", sum

students = [ {"name": "Bob", "score": 90}, {"name": "Terry", "score": 74}]
for student in students:
    print student['name']
    print student['score']
    for score in students:
        if score >= 90:
            print "A"
        elif score = 89 and score >= 80:
            print "B"
        elif score = 79 and >=70:
            print "C"
        else:
            print "You failed and must take the test again."