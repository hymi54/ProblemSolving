from itertools import permutations as per

n, m = map(int, input().split())
for i in per([j for j in range(1, n+1)], m):
    print(*i)