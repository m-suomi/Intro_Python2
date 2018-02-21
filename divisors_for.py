x = int(input('Calculate the divisors of which number? '))

for poss_div in range(1,x+1):
    if x % poss_div == 0:
        print (poss_div)


#a = 1
#while a <= x:
#    if x % a == 0:
#        print (a)
#        a += 1
#    else:
#        a += 1
