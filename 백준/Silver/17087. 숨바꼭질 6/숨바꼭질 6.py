def euclid(a, b):
    if b == 0:
        return a
    if a < b:
        a, b = b, a
    return euclid(b, a % b)


n, s = map(int, input().split())
arr = list(map(lambda x: abs(x-s), map(int, input().split())))

if len(arr) < 2:
    d = arr[0]
else:
    d = euclid(arr[0], arr[1])

for i in range(2, n):
    d = euclid(d, arr[i])

print(d)
