prime_under_ten_thousand = []
prime = [True for _ in range(10001)]

for i in range(2, 101):
    if prime[i]:
        for j in range(i*2, 10001, i):
            prime[j] = False

for i, v in enumerate(prime):
    if v:
        prime_under_ten_thousand.append(i)

for _ in range(int(input())):
    n = int(input())
    for i in range(n//2):
        if n//2-i in prime_under_ten_thousand and n//2+i in prime_under_ten_thousand:
            print(f'{n//2-i} {n//2+i}')
            break
