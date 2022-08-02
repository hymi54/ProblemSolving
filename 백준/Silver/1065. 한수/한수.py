n = int(input())
han_list = [i for i in range(1, 10) if i <= n]


def han(x: int, step: int) -> None:
    if x % 10 + step < 0 or x % 10 + step > 9:
        return None
    new = x * 10 + x % 10 + step
    if new > n or new in han_list:
        return None
    else:
        han_list.append(new)
        han(new, step)
        return None


for i in range(1, 10):
    for st in range(-9, 10):
        han(i, st)

print(len(han_list))
