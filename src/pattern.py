# Print the pattern
for i in range (1,6):
    for j in range(0,i):
        if j == i-1:
            print('*', end='')
        else:
            print('*', end=' ')
    print('')
for i in range (5,1,-1):
    for j in range(0,i-1):
        if j == i-1:
            print('*', end='')
        else:
            print('*', end=' ')
    print('')
