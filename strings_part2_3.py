#Write a script that removes all of the vowels in a user inputted string.

user_string = input('Input user string: ')

#for char in user_string:
    #if char == 'a' or 'e' or 'i' or 'o' or 'u':
        #user_string = user_string.replace(char , '')
        #print(user_string)


user_string = user_string.replace('a' , '')
user_string = user_string.replace('e' , '')
user_string = user_string.replace('i' , '')
user_string = user_string.replace('o' , '')
user_string = user_string.replace('u' , '')


print(user_string)
