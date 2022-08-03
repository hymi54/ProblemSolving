phone_number = list(input())
sum = 0

"""
풀이 1 : 하드코딩
"""
dial = {"ABC": 3, "DEF": 4, "GHI": 5, "JKL": 6, "MNO": 7, "PQRS": 8, "TUV": 9, "WXYZ": 10}

for i in phone_number:
    for k, v in dial.items():
        if i in k:
            sum += v

print(sum)
