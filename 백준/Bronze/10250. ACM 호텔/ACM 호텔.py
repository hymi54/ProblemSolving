for _ in range(int(input())):
    h, w, n = map(int, input().split())
    print(f'{n-h*((n-1)//h)}{(n-1)//h+1:0>2}')
