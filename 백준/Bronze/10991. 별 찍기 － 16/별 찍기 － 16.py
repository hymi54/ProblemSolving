n = int(input())

for i in range(n):
    print(' '*(n-i-1), '*', sep='', end='')
    for j in range(i):
        print(' *', end='')
    print()
