print('\033c')

a = input('Enter a word : ')

for i in a:
    if i == 'a':
        print('a is found')
        break
    
    else:
        print(f'Value of i is {i}\na not found\n')