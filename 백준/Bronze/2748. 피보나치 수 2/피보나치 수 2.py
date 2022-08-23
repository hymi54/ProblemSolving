fib0 = 0
fib1 = 1
fib2 = 1

for _ in range(1, int(input())):
    fib2 = fib0 + fib1
    fib0 = fib1
    fib1 = fib2

print(fib2)
