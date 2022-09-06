
# Print the numbers described in the exercise
for i in range (1,11):
    for j in range(0,i):
        if j == i-1:
            print(j+1, end='')
        else:
            print(j+1, end=' ')
    print('')
     