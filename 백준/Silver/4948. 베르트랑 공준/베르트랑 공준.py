while True:
    n = int(input())
    if not n:
        break
    prime_arr = [True for _ in range(2*n + 1)]

    for i in range(0, 2):
        prime_arr[i] = False

    for i in range(2, int((2*n)**.5)+1):
        if prime_arr[i]:
            for j in range(2*i, 2*n+1, i):
                prime_arr[j] = False

    for i in range(n+1):
        if prime_arr[i]:
            prime_arr[i] = False

    print(prime_arr.count(True))
