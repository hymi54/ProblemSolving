n = int(input())
test_case = []
for _ in range(n):
    test_case.append(input())

for ox in test_case:
    streak = 0
    score = 0
    for s in list(ox):
        if s == 'O':
            streak += 1
            score += streak
        else:
            streak = 0
    print(score)
