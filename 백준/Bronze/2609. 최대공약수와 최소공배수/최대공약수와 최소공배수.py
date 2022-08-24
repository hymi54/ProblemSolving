def euclid(a, b):
    if b == 0:
        return a
    if b > a:
        a, b = b, a

    return euclid(b, a % b)


n, m = map(int, input().split())
print(euclid(n, m))
print(n*m//euclid(n, m))
