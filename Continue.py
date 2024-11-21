print('\033c')

var = 10

while var > 0:
    var = var - 1
    
    if var == 5 or var == 8:
        continue
    
    print('\nCurrent variable value :', var)

print('\nGood Bye!')