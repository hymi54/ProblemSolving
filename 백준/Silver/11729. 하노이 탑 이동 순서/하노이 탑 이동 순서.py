def hanoi(n: int):
    if n == 1:
        return 1
    return hanoi(n-1)*2 + 1


def hanoi_move(n: int, start: int, end: int):
    if n == 0:
        return None

    hanoi_move(n-1, start, 6-start-end)
    print(f'{start} {end}')
    hanoi_move(n-1, 6-start-end, end)
    return None


circle = int(input())
print(hanoi(circle))
hanoi_move(circle, 1, 3)
