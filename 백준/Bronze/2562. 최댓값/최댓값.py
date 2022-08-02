max_int = int(input())
index = 1

for i in range(8):
    input_ = int(input())
    if max_int < input_:
        max_int = input_
        index = i+2

print(max_int, index, sep="\n")
