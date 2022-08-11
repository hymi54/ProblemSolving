n, m = map(int, input().split())
mat = [[0]*m for _ in range(n)]

for _ in range(2):
    for i in range(n):
        li = list(map(int, input().split()))
        for j in range(m):
            mat[i][j] += li[j]

for i in mat:
    print(*i)
