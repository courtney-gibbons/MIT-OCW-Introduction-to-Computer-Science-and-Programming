#Problem Set 2b
#Name: Courtney Gibbons
#Time: 15
#
maxcantbuy = 1 #variable that keeps track of largest number of McNuggets that cannot be bought in exact quantity
x = 6
y = 9
z = 20
packages = (x,y,z) #variable that contains package sizes
maxn = 200
for n in range(1, maxn + 1):
    print('Testing for: ' + str(n))
    canpurchase = 'false' #assume you can't buy it
    for a in range (0, n/packages[0] + 1):
        for b in range (0, n/packages[1] + 1):
            for c in range (0, n/packages[2] + 1):
                if packages[0]*a + packages[1]*b + packages[2]*c == n:
                    canpurchase = 'true' #if one of these combos is true, you can buy it
    if canpurchase == 'false' and n > maxcantbuy: #if you still can't buy it,
        maxcantbuy = n
print('Given package sizes ' + str(x) + ', ' + str(y) + ', and ' + str(z) + ', the largest number of McNuggets that cannot be bought in exact quantity is: ' + str(maxcantbuy))
