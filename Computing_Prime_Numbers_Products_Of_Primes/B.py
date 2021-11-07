#Problem Set 1b
#Name: Courtney Gibbons
#Time: 15
#
import math
count = 1
number = 2
n = 10
#n = int(raw_input('Enter an integer, n, to find the sum of the logs of the first n prime numbers and the ratio to nth prime number: '))
sum = 0
while count < n + 1: #stops after n5
    prime = True #always need to define variables
    div = number - 1
    while div > 1: #no div by 0, div by 1 will have no remainder
        if number%div == 0:
            prime = False
            div = 1 #stops while loop bc div not > 1
        else: 
            div = div - 1 #loops
    if prime == True:
        sum = sum + math.log(number) #need to specify base or does ln
        count = count + 1 #only increase count if prime
        if count == n + 1:
            print('n = ' + str(n))
            print('nth prime = ' + str(number))
            print('sum of the logs of the first n primes = ' + str(sum))
            print('ratio of the sum to the nth prime = ' + str(sum/number))
    number = number + 1 #increase number
