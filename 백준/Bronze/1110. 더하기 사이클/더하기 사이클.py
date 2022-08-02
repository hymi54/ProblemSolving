temp = start = int(input())
new = 10 * (start % 10) + (start // 10 + start % 10) % 10
count = 1

while new != start:
    temp = new
    new = 10 * (temp % 10) + (temp // 10 + temp % 10) % 10
    count += 1

print(count)
