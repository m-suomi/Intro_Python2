user_input = input('What string do you want to add to the list? ')
my_list = [1, 'hello', 2, 'there', 3, 'list']

if len(user_input) < 8:
    my_list.append(user_input)
else:
    my_list.append(4)
print(my_list)
