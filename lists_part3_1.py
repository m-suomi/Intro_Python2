#Write a script that creates a list of only the even numbers between 0 and a user inputted number.

end_num = int(input('What is the end number you are looking at (inclusive) for evens? '))
evens = []

for num in range(end_num+1):
    if num % 2 == 0:
        evens.append(num)

print(evens)
