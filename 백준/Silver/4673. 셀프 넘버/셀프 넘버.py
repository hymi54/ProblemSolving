'''
풀이 1 : 재귀적으로 1부터 10000까지 각 수의 d(n), d(d(n)), ... 을 찾아 제거
'''
ten_thousand = [i for i in range(1, 10000)]


def delete_num(n: int) -> None:
    if n in ten_thousand and n < 10000:
        ten_thousand.remove(n)
        delete_num(n + sum(map(int, list(str(n)))))
    return


for i in ten_thousand:
    delete_num(i + sum(map(int, list(str(i)))))

print('\n'.join(map(str, ten_thousand)))
