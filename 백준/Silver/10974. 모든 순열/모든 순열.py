from itertools import permutations

n = int(input())
int_list = [i for i in range(1, n+1)]

for i in permutations(int_list, n):
    print(*i)
