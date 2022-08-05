n = int(input())
count_3 = 0

while n % 5 != 0:
    n -= 3
    count_3 += 1
    if n < 0:
        print(-1)
        break

if n >= 0:
    print(f'{n//5 +  count_3}')
