#Write a script that makes every other letter of a user inputted string capitalized.
#I'm assuming this includes spaces as characters and doesn't do code to ingnore spaces for alternating caps

user_string = input('Input user string: ')
final_string = ''

for index , char in enumerate(user_string):
    if index % 2 == 0:
        final_string += char.upper()
    else:
        final_string += char  #if want to guarantee every other lower case, change to char.lower()

##FIRST ITERATION
#user_string_cap = user_string.upper()
#index = 0
#for index in range(len(user_string)):
#    if index % 2 == 0:
#        final_string += user_string_cap[index]
#    else:
#        final_string += user_string[index]

print(final_string)


##DIDN'T WORK
#for char in user_string[::2]:
#    print(char)
#    user_string[char] = user_string.upper()[char]

#user_string.replace(user_string[2], user_string.upper()[2])
