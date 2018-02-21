my_list = ['hello', 'there', 'python', list('list'), '!']
longer_elements = []
for index, element in enumerate(my_list):

    if len(element) > 4:
        longer_elements.append(element)
        print(longer_elements)
print(longer_elements)


    ##print odd indices
    #if index%2 != 0:
        #print(index, element)
