def append_star(len_):
    if len_ == 1:
        return ['*']

    stars = append_star(len_ // 3)
    l = []

    for S in stars:
        l.append(S * 3)
    for S in stars:
        l.append(S + ' ' * (len_ // 3) + S)
    for S in stars:
        l.append(S * 3)
    return l


n = int(input())
print('\n'.join(append_star(n)))
