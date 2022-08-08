def kn(k: int, n: int) -> int:
    if k == 0:
        return n
    elif n == 1:
        return 1
    else:
        return kn(k-1, n) + kn(k, n-1)


for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(kn(k, n))
