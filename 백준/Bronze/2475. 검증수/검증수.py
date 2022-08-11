def koi(arr: list[int]):
    sum_ = 0
    for i in arr:
        sum_ += i**2
    return sum_ % 10


print(koi(list(map(int, input().split()))))
