#Given the list [0, 3, 6, 9, 10, 2, 5] and [2, 6, 4, 7, 8, 1, 15], write a script that
#finds the common elements between them. Store them in a list, and print that list, sorted,
#as the final output (if you'd like you can go ahead and hard code those lists in your script).

#Challenge: Alter your script in Part 3, Question 3 to accept arbitrary lists. Build it such that the user
#has to enter 7 numbers (each separated by an enter at the command line) for each list.

lst_1 = []
lst_2 = []

for index in range(0,7):
    user_val = int(input('What is element ' + str(index) + ' of your first list? '))
    lst_1.append(user_val)
for index in range(0,7):
    user_val = int(input('What is element ' + str(index) + ' of your second list? '))
    lst_2.append(user_val)

common_elems = []

for num1 in lst_1:
    for num2 in lst_2:
        if num1 == num2:
            common_elems.append(num1)

common_elems.sort()
print(common_elems)
