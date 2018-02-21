my_list = ['hello', 'there', 'python', list('list'), '!']
for index, element in enumerate(my_list):

    ##print if element is longer than 4 characters
    if len(element) > 4:
        print(index, element)


    ##print odd indices
    #if index%2 != 0:
        #print(index, element)
