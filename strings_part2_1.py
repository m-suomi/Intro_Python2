#Write a script that obtains the count of a user inputted letter in a user inputted string
#(Hint: Use input() twice to get both of the user inputs). Make sure to build this in such
#a way that it ignores the case of the inputted string and letter.

user_letter = input('Input a letter: ')
user_string = input('Input user string: ')
count = 0

for char in user_string.lower():
    if char == user_letter.lower():
        count += 1

print(str(user_letter) + ' appears ' + str(count) + ' times in the user string.')
