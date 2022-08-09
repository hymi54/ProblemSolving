start, end = map(int, input().split())
prime_num = [False, False] + [True] * (end-1)

for i in range(2, int(end**.5)+1):
    if prime_num[i]:
        for j in range(i*2, end+1, i):
            prime_num[j] = False

for i in range(start, end+1):
    if prime_num[i]:
        print(i)
