#For a user inputted number, write a script that outputs a list of multiples of that number
#from 0 up to another user inputted number. For example, given the numbers 4 and 20, your
#script should print the numbers 4, 8, 12, and 16.

user_multiple = int(input('Which number would you like to find multiples of? '))
user_end = int(input('You want to calculate multiples up to what number (inclusive)? '))
multiples = []
index = 1

while index <= user_end/user_multiple:
    multiples.append(user_multiple * index)
    index += 1

print(multiples)
