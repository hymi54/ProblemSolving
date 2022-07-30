"""
1번 풀이 : 처음부터 정수로 캐스팅한 다음 모듈로 연산 활용
"""
# int_a = int(input())
# int_b = int(input())
#
# int_3 = int_a * (int_b % 10)
# int_4 = int_a * ((int_b % 100) // 10)
# int_5 = int_a * (int_b // 100)
# int_6 = int_a * int_b
#
# print(int_3, int_4, int_5, int_6, sep='\n')

"""
2번 풀이 : 문자열로 입력받은 다음 인덱싱으로 해결
"""

a = input()
b = input()

int_3 = int(a) * int(b[2])
int_4 = int(a) * int(b[1])
int_5 = int(a) * int(b[0])
int_6 = int(a) * int(b)

print(int_3, int_4, int_5, int_6, sep='\n')
