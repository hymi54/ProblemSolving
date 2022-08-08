total = int(input())
sum_ = 0

for _ in range(int(input())):
    price, num = map(int, input().split())
    sum_ += price*num

if sum_ == total:
    print('Yes')
else:
    print('No')
