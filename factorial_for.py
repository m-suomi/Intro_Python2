#with for instaead of while
input = int(input('Please input the number you want to find the factorial of: '))
total = 1
#while input > 1:
    #total *= input
    #print(input, total)
    #input -= 1
#print(total)

for term in range(1,input+1):
    total *= term
    print(term, total)
print(total)
