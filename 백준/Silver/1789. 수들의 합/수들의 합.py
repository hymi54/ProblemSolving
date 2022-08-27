s = int(input())
sum_ = 0
i = 0

while sum_ < s:
    i += 1
    sum_ += i

if sum_ == s:
    print(i)
else:
    print(i-1)
