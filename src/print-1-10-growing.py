
# Print the numbers described in the exercise
for i in range (1,12):
    for j in range(1,i):
        if j == i-1:
            print(j, end='')
        else:
            print(j, end=' ')
    print('')
