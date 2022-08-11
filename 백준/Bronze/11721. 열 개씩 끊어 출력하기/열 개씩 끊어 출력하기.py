s = input()

for i, v in enumerate(s):
    if i % 10 == 0 and i != 0:
        print()
    print(v, end='')
