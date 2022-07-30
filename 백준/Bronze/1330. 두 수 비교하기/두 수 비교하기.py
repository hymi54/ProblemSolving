int_A, int_B = map(int, input().split())

if int_A > int_B:
    print('>')
elif int_A < int_B:
    print('<')
else:  # int_A == int_B
    print('==')
