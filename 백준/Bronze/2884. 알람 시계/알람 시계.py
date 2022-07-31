h, m = map(int, input().split())

if m - 45 < 0:
    m += 15
    h -= 1
else:
    m -= 45

if h < 0:
    h += 24

print(h, m)
