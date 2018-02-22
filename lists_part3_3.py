#Given the list [0, 3, 6, 9, 10, 2, 5] and [2, 6, 4, 7, 8, 1, 15], write a script that
#finds the common elements between them. Store them in a list, and print that list, sorted,
#as the final output (if you'd like you can go ahead and hard code those lists in your script).

lst_1 = [0, 3, 6, 9, 10, 2, 5]
lst_2 = [2, 6, 4, 7, 8, 1, 15]
common_elems = []

for num1 in lst_1:
    for num2 in lst_2:
        if num1 == num2:
            common_elems.append(num1)

common_elems.sort()
print(common_elems)
