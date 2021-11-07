#Problem Set 1a
#Name: Courtney Gibbons
#Time: 2:00
#
count = 1
number = 2
while count < 1001: #stops after count 1000
    prime = True #always need to define variables
    div = number - 1
    while div > 1: #no div by 0, div by 1 will have no remainder
        if number%div == 0:
            prime = False
            div = 1 #stops while loop bc div not > 1
        else: 
            div = div - 1 #loops
    if prime == True:
        print(str(count) + ' : ' + str(number))
        if count == 1000:
            print('The 1000th prime number is ' + str(number))
        count = count + 1 #only increase count if prime
    number = number + 1 #increase number

#print('1 : 2')
#count = 2 #starts count at 2 bc 2 = 1st prime
#number = 3 #starts numbers at 3 bc 2 is even
#if number%2 == 1: #weeds out evens
#    while count < 1001: #stops when count = 1000
#        prime = True #always need to define variables
#        div = number - 1
#        while div > 1: #no div by 0, div by 1 will have no remainder
#            if number%div == 0:
#                prime = False
#                div = 1 #stops while loop bc div not > 1
#            else: 
#                div = div - 1 #loops
#        if prime == True:
#            print(str(count) + ' : ' + str(number))
#            if count == 1000:
#                print('The 1000th prime number is ' + str(number))
#            count = count + 1 #only increase count if prime
#        number = number + 1 #increase number
