v_k, j_k = map(int, input().split())
v_l, j_l = map(int, input().split())
v_h, d_h, j_h = map(int, input().split())

print((v_k*j_k + v_l*j_l) * (v_h*d_h*j_h))
