start = int(input())
end = int(input())
prime_arr = []

for i in range(start, end+1):
    if i == 1:
        continue
    j = 2
    while True:
        if j > i**(1/2):
            prime_arr.append(i)
            break
        if i % j == 0:
            break
        j += 1

if prime_arr:
    print(sum(prime_arr), min(prime_arr), sep='\n')
else:
    print(-1)
