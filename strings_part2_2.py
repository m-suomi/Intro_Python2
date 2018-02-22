#Write a script that checks if a user inputted string ends in an exclamation point. If it does,
#then print the string in all capital letters. If it doesn't, print the string in all lowercase letters.

user_string = input('Input user string: ')
exclamation = False

if user_string[-1] == '!':
    exclamation = True

if exclamation:
    print(user_string.upper())
else:
    print(user_string.lower())
