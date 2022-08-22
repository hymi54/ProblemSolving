x, y, w, h = map(int, input().split())

print(min(map(abs, (x-w, x-0, y-h, y-0))))
