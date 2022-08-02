n = int(input())
origin_score = list(map(int, input().split()))

m = max(origin_score)
new_score = list(map(lambda x: x/m*100, origin_score))

print(sum(new_score)/n)
