num_list = [0, 0] + [i for i in range(2, 1000000)]
for i in range(2, 1000):
    if num_list[i]:
        for j in range(2*i, 1000000, i):
            num_list[j] = 0
prime_list = [i for i in num_list if i]

while True:
    n = int(input())
    a = 2
    b = n-2
    if not n:
        break

    while a <= n//2:
        if num_list[a] and num_list[b]:
            break
        else:
            a += 1
            b -= 1
    else:
        print("Goldbach's conjecture is wrong.")
        continue

    print(f'{n} = {a} + {b}')