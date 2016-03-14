#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.


def test(next_number, numbers_list, highest, lowest, num):
    try:
        next_number = int(next_number)
    except:
        next_number = num
        new_number(numbers_list, highest, lowest, num)
    else:
        numbers_list.append(int(next_number))
        
def done(numbers_list, highest, lowest):
    print "Here's a list of the numbers you entered: %r" % numbers_list
    print "The highest number you entered is: %d" % highest
    print "The lowest number you entered is: %d" % lowest
        
def new_number(numbers_list, highest, lowest, num):
    print "Please enter another number:"
    next_number = raw_input("> ")
    number = next_number
    if number == 'done':
        done(numbers_list, highest, lowest)
    else:
        test(next_number, numbers_list, highest, lowest, num)
        
def main():
    numbers_list = []
    highest = 0
    lowest = None
    print "Please enter a number: "
    numbers = raw_input("> ")
    try:
        numbers = int(numbers)
    except:
        numbers = -1
    
    numbers_list.append(numbers)
    
    for num in numbers_list:
        if num > highest:
            highest = num
        
        if lowest is None or num < lowest:
            lowest = num
     
        new_number(numbers_list, highest, lowest, num)
        
main()