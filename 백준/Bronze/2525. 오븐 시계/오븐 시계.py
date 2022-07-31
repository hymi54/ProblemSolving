h, m = map(int, input().split())
cook_time = int(input())

present_time = h * 60 + m
fin_time = present_time + cook_time

fin_h, fin_m = divmod(fin_time, 60)
if fin_h >= 24:
    fin_h -= 24

print(fin_h, fin_m)
