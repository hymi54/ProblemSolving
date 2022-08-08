input()
arr = map(int, input().split())
count = 0

for i in arr:
    if i == 1:
        continue
    j = 2

    while True:
        if j > i**(1/2):
            count += 1
            break
        if i % j == 0:
            break
        j += 1

print(count)
