n = 0
x = int(input())

while n*(n+1)/2 < x:
    n += 1

if n % 2 == 0:
    print(f'{int(n-(n*(n+1)/2-x))}/{int(1+(n*(n+1)/2-x))}')
else:
    print(f'{int(1+(n*(n+1)/2-x))}/{int(n-(n*(n+1)/2-x))}')
