s = input().upper()
res = {}

for i in set(s):
    res[i] = s.count(i)

if list(res.values()).count(max(res.values())) > 1:
    print('?')
else:
    print([k for k, v in res.items() if v == max(res.values())][0])
