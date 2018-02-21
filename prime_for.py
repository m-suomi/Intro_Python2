#check if number is prime or not

#use for instead of while loops
x = int(input('Please input your number: '))
prime = True

for integer in range(2,x):
    if x % integer == 0:
        prime = False
        break

if prime:
    print(str(x) + ' is a prime number.')
else:
    print(str(x) + ' is NOT a prime number.')


#a = x - 1
#while a > 1:
#    if x % a == 0:
#        print(str(x) + ' is not a prime number.')
#        break
#    else:
#        a -= 1
#if a == 1:
#    print(str(x) + ' is a prime number.')
