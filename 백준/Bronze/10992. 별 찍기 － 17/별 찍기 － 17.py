n = int(input())

for i in range(n-1):
    print(' '*(n-i-1), '*', ' '*(2*i-1), end='', sep='')
    if i:
        print('*')
    else:
        print()
print('*'*(2*n-1))
