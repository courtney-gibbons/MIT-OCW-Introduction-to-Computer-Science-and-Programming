#Problem Set 2a
#Name: Courtney Gibbons
#Time: 1:00
#
#maxcantbuy = 0 #variable that keeps track of largest number of McNuggets that cannot be bought in exact quantity
#packages = (6,9,20) #variable that contains package sizes
#maxn = 150
#maxa = maxn/packages[0]
#maxb = maxn/packages[1]
#maxc = maxn/packages[2]
#
#for n in range(1, maxn + 1): #only search for solutions up to size 150
#    print('Testing for n = ' + str(n))
#    canpurchase = 'false'
#    for a in range (0, maxa + 1):
#        for b in range (0, maxb + 1):
#            for c in range (0, maxc + 1):
#                if packages[0]*a + packages[1]*b + packages[2]*c == n:
#                    canpurchase = 'true'
#    if canpurchase == 'false' and n > maxcantbuy:
#        maxcantbuy = n
#print('The largest number of McNuggets that cannot be bought is ' + str(maxcantbuy))

n = 1
maxcantbuy = 1 #variable that keeps track of largest number of McNuggets that cannot be bought in exact quantity
packages = (6,9,20) #variable that contains package sizes
while n < maxcantbuy + 6 + 1:
    print('Testing for: ' + str(n))
    canpurchase = 'false' #assume you can't buy it
    for a in range (0, n/packages[0] + 1):
        for b in range (0, n/packages[1] + 1):
            for c in range (0, n/packages[2] + 1):
                if packages[0]*a + packages[1]*b + packages[2]*c == n:
                    canpurchase = 'true' #if one of these combos is true, you can buy it
    if canpurchase == 'false' and n > maxcantbuy: #if you still can't buy it,
        maxcantbuy = n
    n = n + 1
print('Largest number of McNuggets that cannot be bought in exact quantity: ' + str(maxcantbuy))
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
