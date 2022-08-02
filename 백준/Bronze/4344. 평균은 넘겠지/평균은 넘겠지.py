for _ in range(int(input())):
    n, *test_case = map(int, input().split())
    avg = sum(test_case) / n
    over_avg = 0
    for score in test_case:
        if score > avg:
            over_avg += 1
    print(f'{over_avg/n*100:.3f}%')
