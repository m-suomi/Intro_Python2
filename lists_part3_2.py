#Write a script that creates a list of only numbers divisible by a user inputted number
# that are between 0 and a user inputted number (Hint: Use input() twice to get both of the user inputs).

divisor = int(input('What is the number you are dividing by? '))
end_num = int(input('What is the end number you are looking at (inclusive) for numbers divisible by ' + str(divisor) + '? '))
divis_nums = []

for num in range(end_num+1):
    if num % divisor == 0:
        divis_nums.append(num)

print(divis_nums)
