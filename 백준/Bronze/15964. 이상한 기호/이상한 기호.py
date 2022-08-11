def plus_mul_minus(a: int, b: int):
    return (a+b)*(a-b)


a, b = map(int, input().split())
print(plus_mul_minus(a,b))
