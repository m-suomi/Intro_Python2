user_number = int(input('Min length to be printed: '))
my_list = ['hello', 'there', 'python', list('list'), '!']
longer_elements = []
for index, element in enumerate(my_list):

    if len(element) >= user_number:
        longer_elements.append(element)
        #print(longer_elements)
print(longer_elements)
