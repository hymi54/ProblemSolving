n = int(input())
floor_sum = -1
floor = 0

while floor_sum < (n-2) // 6:
    floor += 1
    floor_sum += floor

print(floor+1)
